package client;

import java.util.HashMap;

import api.LocalityServiceAPI;

public class LocalityServiceClient {
	
	public static void main(String args[]){
		LocalityServiceAPI lsAPI = new LocalityServiceAPI( System.getProperty("user.dir")+"/src/client/location_service_cfg.yaml");
		int id = lsAPI.insert(7.1, 6.5, 0.9, "Rons JavaInsert");
		System.out.println("Got Id "+id+" Now try updating the entry");
		boolean updateResult = lsAPI.update(id, 7.2, 6.6, 1.0, "Rons Updated Insert");
		System.out.println("Update "+updateResult+" Now try deleteing");
		boolean result = lsAPI.delete(id);
		System.out.println("Delete "+result+" Now lets try a parameter search");
		int[] ids = lsAPI.search(48.0, 142.0, 55.0, 2.0, 2.0, 10.0, null);
		for(int i: ids){
			System.out.print(i+" ");
		}
		System.out.println("\nNow Search by Name");
		int[] ides = lsAPI.search(null, null, null, null, null, null, "RigiLab2");
		for(int i: ides){
			System.out.print(":"+i+" ");
			HashMap info = lsAPI.get(i);
			if(info != null){
				System.out.print(info);
			}
		}
	}
}
