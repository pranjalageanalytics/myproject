
$(document).ready(function(){
	

        $("#submit_frm").click(function(event){
        	alert("in js called method");
        	//event.preventDefault();
        	var datevalue = document.getElementById('datepicker').value
        	//alert("date value is -- " + datevalue);
        	
        	var emailvalue = document.getElementById("id_email").value
        	//alert("email value is -- " + emailvalue);
        	
        	var contactvalue = document.getElementById("contact").value
        	//alert("contact value is -- " + contactvalue);
        	
        	var passvalue = document.getElementById("pass").value
        	//alert(" value is -- " + passvalue);
        	
        	var passvalue1 = document.getElementById("pass2").value
        	//alert(" value is -- " + passvalue1);
        	
    		flag = true;
    		
    	//Validation for Gender Starts 	
   		 if($('input[name=gender]:checked').length<=0)
   	        {
   	        	 document.getElementById('error5').innerHTML=" This field is required!";
   			     

   				   flag=false;
   	        }
   		 else{
   			 
   			 $("#error5").hide();
   		   
   		     }
        //Validation for Gender Ends
        
     	//Validation for Gifter Date starts
 		if(datevalue==""){
 			alert("in date if");
  			$("#date1").show();
  			
  			   document.getElementById('date1').innerHTML=" This field is required!";
  				document.getElementById("datepicker").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
		
		 else{
             
             $("#date1").hide();
             
               document.getElementById("datepicker").style.borderColor = "#ccc";
             }
     	//Validation for Gifter Date Ends
 		
 		if(emailvalue=="")
		{
  			  alert("in if");
			   $("#error_email").show();
  			
  			   document.getElementById('error_email').innerHTML=" This field is required!";
  			   document.getElementById("id_email").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
		
          
          var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
          
          if(emailvalue!=""){
              if(reg.test(emailvalue) == false) {
             
               $("#error_email").show();
             document.getElementById('error_email').innerHTML="Invalid Email";
             document.getElementById("id_email").style.borderColor = "#E34234";
            flag=false;
            	//alert("in email if "+flag);
             
                  }
           
  		    else{
             //flag=true;
  			//alert("else of email");
             $("#error_email").hide();
               document.getElementById("id_email").style.borderColor = "#ccc";
              
             }
             }
 		
          
          if(contactvalue==""){
  			$("#error2").show();
  			//alert("in contact")
  			   document.getElementById('error2').innerHTML=" This field is required!";
  				document.getElementById("contact").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
  	  else{
            //flag=true;
 			//alert("else of email")
            $("#error2").hide();
            
              document.getElementById("contact").style.borderColor = "#ccc";
            }
  	  
  	  var re =/^[- +()]*[0-9][- +()0-9]*$/
  	  if(contactvalue!=""){
            if(!re.test(contactvalue)) {
           
             $("#error2").show();
           document.getElementById('error2').innerHTML="Contact number contains only digits";
           document.getElementById("contact").style.borderColor = "#E34234";
          flag=false;
          	//alert("in email if "+flag);
           
                }
            if(contactvalue.length!=12)
            {
                //alert("in length");
                $("#error2").show();
              document.getElementById('error2').innerHTML="Contact number must be 12 digits";
              document.getElementById("contact").style.borderColor = "#E34234";
             flag=false;
             	//alert("in email if "+flag);
              
                   }
  	  }
		    
  	  
  	 if(passvalue==""){
   	  
	        document.getElementById('error_pass').innerHTML=" This field is required!";
	        document.getElementById("pass").style.borderColor = "#E34234";

	   flag=false;
	   //alert(pass1.value);
	   }
	  
	  if(passvalue != "") {
	   
	         if(passvalue.length < 8) {
	          console.log("length is less");
	     document.getElementById('error_pass').innerHTML=" Password must contain at least Eight characters!";
	     document.getElementById("pass").style.borderColor = "#E34234";
	       // document.getElementById("pass2").style.borderColor = "#E34234";
	           
	           flag=false;
	         }
	         
	         
	         else if(!(re = /[0-9]/).test(passvalue)) {
	          console.log("Number");
	        document.getElementById('error_pass').innerHTML=" password must contain at least one number (0-9)!";
	     document.getElementById("pass").style.borderColor = "#E34234";
	     //document.getElementById("pass2").style.borderColor = "#E34234";
	           
	           flag=false;
	         }
	         
	         else if(!(re = /[a-z]/).test(passvalue)) {
	          console.log("lowercase");
	        document.getElementById('error_pass').innerHTML=" password must contain at least one lowercase letter (a-z)!";
	     document.getElementById("pass").style.borderColor = "#E34234";
	           
	           flag=false;
	         }
	         
	         else if(!(re = /[A-Z]/).test(passvalue)) {
	          console.log("uppercase");
	     document.getElementById('error_pass').innerHTML=" password must contain at least one uppercase letter (A-Z)!";
	     document.getElementById("pass").style.borderColor = "#E34234";
	           
	           flag=false;
	         }
	         else if(!(re = /[_\-!\"@;,.:]/).test(passvalue)) {
	          console.log("special char");
	     document.getElementById('error_pass').innerHTML=" password must contain at least one special character!";
	     document.getElementById("pass").style.borderColor = "#E34234";
	           
	           flag=false;
	         }
	         else
	          {
	          document.getElementById('error_pass').innerHTML=" ";
	          document.getElementById("pass").style.borderColor = "#ccc";
	          }
	       }
	
        
	  if(passvalue1==""){
 			// alert("pass2")
		    document.getElementById('error4').innerHTML=" This field is required!";
		         document.getElementById("pass2").style.borderColor = "#E34234";

		    flag=false;
		    //alert(pass2.value);
		    }
 		 else
		     {
		   document.getElementById('error4').innerHTML=" ";
		   document.getElementById("pass2").style.borderColor = "#ccc";
		     }
 		 if (passvalue1!="")
 			 {
 			 
 			
		  if (passvalue1!=passvalue) {
		         
		         document.getElementById('error4').innerHTML=" Password and confirm password must be same!";
		         //document.getElementById("pass1").style.borderColor = "#E34234";
		         document.getElementById("pass2").style.borderColor = "#E34234";
		         flag=false;
		          }
 			 }
	  
	  
 		  return flag;
        });
		
          
       
 		 
		
	
   
});    



