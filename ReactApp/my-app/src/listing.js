export default {
 getJSONListing(searchTerm,scoreOrViewCount) {
     let request=process.env.host.toString()+'/'
     if(searchTerm==="" & scoreOrViewCount===-1){
                // fetch the request normally
     }
     else{
         request=request+'?'
         if(scoreOrViewCount===0) {
          request=request+'type=score';
         }
         else if(scoreOrViewCount===1) {
             request = request + 'type=viewCount';
         }
        if(searchTerm!=="") {
            request=request+'&searchTerm='+searchTerm;}
     }

   return fetch(request).then(response => response.json());
 }
}