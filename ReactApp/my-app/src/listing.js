import {BASE_URI} from "./apiClient";

export default {
 getJSONListing(searchTerm,scoreOrViewCount) {
     let request=BASE_URI+'/'

     if(searchTerm.length==0 & scoreOrViewCount===-1){
                // fetch the request normally

     }
     else{
         request=request+'?'
         if(scoreOrViewCount==0) {
          request=request+'type=score';
         }
         else if(scoreOrViewCount==1) {
             request = request + 'type=viewCount';
         }
        if(searchTerm.length!=0) {
            request=request+'&searchTerm='+searchTerm;}
     }


   return fetch(request).then(response => response.json());
 }
}