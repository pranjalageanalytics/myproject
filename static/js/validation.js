
$(document).ready(function(){
	//alert("hiii");
	$("#login-form").click(function(){
		//alert("hiii in click");
		flag = true;
		if(email.value==""){
  			$("#error1").show();
  			
  			   document.getElementById('error1').innerHTML=" This field is required!";
  			   document.getElementById("email").style.borderColor = "#E34234";
  			   flag=false;
  			   
  			  }    
             
  		    else{
            
             $("#error1").hide();
               document.getElementById("email").style.borderColor = "#ccc";
             } 
          
		 if(pass3.value==""){
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
   


