
$(document).ready(function(){
	//alert("hiii");
	$("#login-form").click(function(){
		//alert("hiii in click");
		
		var emailvalue = document.getElementById('email').value
    	//alert("date value is -- " + emailvalue);
		
		var passvalue = document.getElementById('pass3').value
    	//alert("date value is -- " + passvalue);
		
		flag = true;
		
			
		if(emailvalue==""){
  			$("#error1").show();
  			
  			   document.getElementById('error1').innerHTML=" This field is required!";
  			   document.getElementById("email").style.borderColor = "#E34234";
  			   flag=false;
  			   
  			  }    
             
  		    else{
            
             $("#error1").hide();
               document.getElementById("email").style.borderColor = "#ccc";
             } 
          
		 if(passvalue==""){
			    $("#error3").show();
	   		       document.getElementById('error3').innerHTML=" This field is required!";
	   		        document.getElementById("pass3").style.borderColor = "#E34234";

	   		   flag=false;
	   		   //alert(pass1.value);
	   		   }
	   		  
   		  
          else{
              
              $("#error3").hide();
                document.getElementById("pass3").style.borderColor = "#ccc";
              }
              
   		
   		 
         // alert(flag);
          return flag;
          
	});
       
});    
   


