package client;

public class JSONFactory {
	public static String createInsert(double lat,double lng,double height,String name){
		return "{\"lat\":"+lat+",\"lng\":"+lng+",\"height\":"+height+",\"name\":\""+name+"\"}";
	}
	
	public static String createUpdate(int id,double lat,double lng,double height,String name){
		return "{\"id\":"+id+",\"lat\":"+lat+",\"lng\":"+lng+",\"height\":"+height+",\"name\":\""+name+"\"}";
	}
	
	public static String createSearch(Double lat, Double lng, Double height, Double latRng, Double lngRng, Double heightRng,String name){
		//return '{"lat":%s,"lng":%s,"height":%s,"lat_rng":%s,"lng_rng":%s,"height_rng":%s}'%(lat,lng,height,lat_rng,lng_rng,height_rng)
	    if (name == null){
	    	return "{\"lat\":"+lat+",\"lng\":"+lng+",\"height\":"+height+",\"lat_rng\":"+latRng+",\"lng_rng\":"+lngRng+",\"height_rng\":"+heightRng+" }";
	    }else{
	    	return "{\"name\":\""+name+"\"}";
	    }
	}
	
	public static String createDelete(int id){
		return "{\"id\":"+id+"}";
	}
	
	public static String createGet(int id){
		return "{\"id\":"+id+"}";
	}
}
