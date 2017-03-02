$(document).ready(function(){
//	var someObj={};
//	var location=[];
//	var p; 	

  //alert("get........");
console.log("in category js");
 //#################end checkbox #############
	allValues=[]
	$("#categoryclick").click(function(e){
		//alert("in category js");
		//console.log('within form submit');
		//allValues=[]
		var checkboxes=$("#cat").contents().find(':checkbox');
	     //console.log(checkboxes); 
	     for (var i = 0; i < checkboxes.length; i++)
	        {
	            if(checkboxes[i].checked==true)
	            	{
	            		console.log('k',checkboxes[i].value);
	            		allValues.push(checkboxes[i].value)
	            		var cat=allValues.toString();
	            	}
	        }
		//var state = $("#iframe").contents().find(":checkbox").is(":checked");
		 //console.log('checkboxes',cat)
	   
	         var len= allValues.length
      
                 if(len>0){
  
		 $.ajax({
			 
		   url : '/home/category_save/',
		   type : "POST",
		   data : {'cat':cat},
		   dataType: 'json',
		   traditional: true,
            }).done(function(data) {
//            	                        
	       })
	       //alert("for save");
		 $('#category-form').submit()
		 //alert("after save");
		 window.location.href="http://192.168.1.129:8043/home/challenge/"
     }
   
   else
   {
    var a = document.getElementById("demo1");
	   a.style.cssText= 'font-size: 20px; cursor: pointer; text-align:center;color:red;';
	   a.innerHTML = 'Please select atleast one category';
	   $("#demo1").show(); 
       
      // alert("Please Selected Atleast One Category")
       
     
    }
	       //$("#myModal").modal('hide');
	       //e.preventDefault();
		});
	
	
});
