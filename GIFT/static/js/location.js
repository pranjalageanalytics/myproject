

$(document).ready(function(){
//	var someObj={};
//	var location=[];
//	var p; 	

  //alert("get........");

 //#################end checkbox #############
	allValues=[]
	$("#locationclick").click(function(e){
		//alert("click");
		console.log('within form submit');
		//allValues=[]
		var checkboxes=$("#demo").contents().find(':checkbox');
	     console.log(checkboxes); 
	     for (var i = 0; i < checkboxes.length; i++)
	        {
	            if(checkboxes[i].checked==true)
	            	{
	            		console.log('k'+checkboxes[i].value);
	            		allValues.push(checkboxes[i].value)
	            		var loc=allValues.toString();
	            	}
	        }
	     //alert("loop")
		//var state = $("#iframe").contents().find(":checkbox").is(":checked");
	     
	     //console.log('checkboxes'+loc)
	   
    var len= allValues.length
        //alert('length'+len)
      
        if(len>0){
	     
  
		 $.ajax({
		   url : '/home/location_save/',
		   type : "POST",
		   data : {'loc':loc},
		   dataType: 'json',
		   traditional: true,
		   
            }).done(function(data) {
            	//alert("nsjhdshdjhsji");
            	
 	       })
 	       //alert("in location");
	       $('#location-form').submit()
	       window.location.href="http://192.168.1.129:8063/home/category/"
	}
       else {
    	   var a = document.getElementById("demo1");
    	   a.style.cssText= 'font-size: 20px; cursor: pointer; text-align:center;color:red;';
    	   a.innerHTML = 'Please select atleast one location';
    	   $("#demo1").show();       
     
      }

	         //e.preventDefault();
           		
          
         // window.reload();		
           
		});
	     
	 
	     
	
});



