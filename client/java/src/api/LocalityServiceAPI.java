package api;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.yaml.snakeyaml.Yaml;

import client.JSONFactory;

public class LocalityServiceAPI {
	private String url = "";
	
	public LocalityServiceAPI(String fileName){
		Yaml yfile = new Yaml();
		String fis = this.getInputStream(fileName);
		
		@SuppressWarnings("unchecked")
		LinkedHashMap<String, String> ymalCnts = (LinkedHashMap<String, String>) yfile.load(fis);
		
		this.url = (String) ymalCnts.get("location-service-url");
	}
	
	public int insert(double lat,double lng,double height,String name){
		String jsonMsg = JSONFactory.createInsert(lat, lng, height, name);
		String urlMsg = this.url+"/insert/?jsonMsg="+URLEncoder.encode(jsonMsg)+"&sid=9890987";
		String httpResult = this.getHttpRequest(urlMsg);
		try {
			JSONObject jobj = new JSONObject(httpResult);
			return jobj.getInt("id");
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return -1;
	}
	
	public boolean delete(int id){
		String jsonMsg = JSONFactory.createDelete(id);
		String urlMsg = this.url+"/delete/?jsonMsg="+URLEncoder.encode(jsonMsg)+"&sid=9890987";
		String httpResult = this.getHttpRequest(urlMsg);
		try {
			JSONObject jobj = new JSONObject(httpResult);
			System.out.println(jobj.toString());
			return !jobj.getBoolean("Error");
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return false;
	}
	
	public boolean update(int id,double lat,double lng,double height,String name){
		String jsonMsg = JSONFactory.createUpdate(id,lat, lng, height, name);
		String urlMsg = this.url+"/update/?jsonMsg="+URLEncoder.encode(jsonMsg)+"&sid=9890987";
		String httpResult = this.getHttpRequest(urlMsg);
		try {
			JSONObject jobj = new JSONObject(httpResult);
			return !jobj.getBoolean("Error");
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return false;
	}
	
	//points = api_inst.search(lat=47.0,lng=141.0,height=50,lat_rng=1,lng_rng=1,height_rng=10)
	public int[] search(Double lat,Double lng,Double height,Double latRng,Double lngRng,Double heightRng,String name){
		String jsonMsg = JSONFactory.createSearch(lat, lng, height, latRng, lngRng, heightRng, name);
		String urlMsg = this.url+"/search/?jsonMsg="+URLEncoder.encode(jsonMsg)+"&sid=9890987";
		String httpResult = this.getHttpRequest(urlMsg);
		try {
			//System.out.println(httpResult);
			JSONArray jobj = new JSONArray(httpResult);
			//System.out.println(jobj);
			int[] retIDs = new int[jobj.length()];
			for(int i=0;i<jobj.length();i++){
				JSONObject jo = jobj.getJSONObject(i);
				retIDs[i] = jo.getInt("id");
			}
			return retIDs;
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return (new int[0]);
	}
	
	public HashMap get(int id){
		String jsonMsg = JSONFactory.createGet(id);
		String urlMsg = this.url+"/get/?jsonMsg="+URLEncoder.encode(jsonMsg)+"&sid=9890987";
		String httpResult = this.getHttpRequest(urlMsg);
		try {
			JSONObject jobj = new JSONObject(httpResult);
			//System.out.println("Getting "+jobj.getJSONObject("info").toString() );
			Iterator it = jobj.getJSONObject("info").keys();
			HashMap dict = new HashMap();
			while(it.hasNext()){
				Object key = it.next();
				dict.put(key, jobj.getJSONObject("info").get((String) key) );
			}
			
			return dict;
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return null;
	}
	
	private String getHttpRequest(String urlToRead) {
		//System.out.println("Connect to "+urlToRead);
		URI uri;
		HttpURLConnection conn;
		BufferedReader rd;
		String line;
		String result = "";
		try {
			uri = new URI(urlToRead);
			//String req = URLEncoder.encode(urlToRead);
			URL url = uri.toURL();
			conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");
			rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
			while ((line = rd.readLine()) != null) {
				result += line;
			}
			rd.close();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return result;
   }

	
	
	private String getInputStream(String fileName){
		File file = new File(fileName);
		FileInputStream fis = null;
 
		try {
			fis = new FileInputStream(file);
 
			String docString = "";
			int content;
			while ((content = fis.read()) != -1) {
				docString = docString.concat(""+((char) content));
			}
			fis.close();
			return docString;
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (fis != null)
					fis.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
		return null;
	}
}
