
$(document).ready(function(){
	$("#submit_frm").click(function(){
		flag = true;
		
		 if($('input[name=gender]:checked').length<=0)
	        {
	        	 document.getElementById('error5').innerHTML=" This field is required!";
			     

				   flag=false;
	        }
		 else{
			 
			 $("#error5").hide();
		   
		     }
		
		
		if(datepicker.value==""){
  			$("#date1").show();
  			
  			   document.getElementById('date1').innerHTML=" This field is required!";
  				document.getElementById("datepicker").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
		
		 else{
             
             $("#date1").hide();
             
               document.getElementById("datepicker").style.borderColor = "#ccc";
             }

		if(id_email.value==""){
  			  
			   $("#error_email").show();
  			
  			   document.getElementById('error_email').innerHTML=" This field is required!";
  			   document.getElementById("id_email").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
		
          
          var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
          
          if(id_email.value!=""){
              if(reg.test(id_email.value) == false) {
             
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
          
        	  if(contact.value==""){
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
        	  if(contact.value!=""){
                  if(!re.test(contact.value)) {
                 
                   $("#error2").show();
                 document.getElementById('error2').innerHTML="Contact number contains only digits";
                 document.getElementById("contact").style.borderColor = "#E34234";
                flag=false;
                	//alert("in email if "+flag);
                 
                      }
                  if(contact.value.length!=12)
                  {
                      //alert("in length");
                      $("#error2").show();
                    document.getElementById('error2').innerHTML="Contact number must be 12 digits";
                    document.getElementById("contact").style.borderColor = "#E34234";
                   flag=false;
                   	//alert("in email if "+flag);
                    
                         }
        	  }
      		    
                 
        
          if(pass.value==""){
        	  
   		        document.getElementById('error_pass').innerHTML=" This field is required!";
   		        document.getElementById("pass").style.borderColor = "#E34234";

   		   flag=false;
   		   //alert(pass1.value);
   		   }
   		  
   		  if(pass.value != "") {
   		   
   		         if(pass.value.length < 8) {
   		          console.log("length is less");
   		     document.getElementById('error_pass').innerHTML=" Password must contain at least Eight characters!";
   		     document.getElementById("pass").style.borderColor = "#E34234";
   		       // document.getElementById("pass2").style.borderColor = "#E34234";
   		           
   		           flag=false;
   		         }
   		         
   		         
   		         else if(!(re = /[0-9]/).test(pass.value)) {
   		          console.log("Number");
   		        document.getElementById('error_pass').innerHTML=" password must contain at least one number (0-9)!";
   		     document.getElementById("pass").style.borderColor = "#E34234";
   		     //document.getElementById("pass2").style.borderColor = "#E34234";
   		           
   		           flag=false;
   		         }
   		         
   		         else if(!(re = /[a-z]/).test(pass.value)) {
   		          console.log("lowercase");
   		        document.getElementById('error_pass').innerHTML=" password must contain at least one lowercase letter (a-z)!";
   		     document.getElementById("pass").style.borderColor = "#E34234";
   		           
   		           flag=false;
   		         }
   		         
   		         else if(!(re = /[A-Z]/).test(pass.value)) {
   		          console.log("uppercase");
   		     document.getElementById('error_pass').innerHTML=" password must contain at least one uppercase letter (A-Z)!";
   		     document.getElementById("pass").style.borderColor = "#E34234";
   		           
   		           flag=false;
   		         }
   		         else if(!(re = /[_\-!\"@;,.:]/).test(pass.value)) {
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
   		 if(pass2.value==""){
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
   		 if (pass2.value!="")
   			 {
   			 
   			
 		  if (pass2.value!=pass.value) {
 		         
 		         document.getElementById('error4').innerHTML=" Password and confirm password must be same!";
 		         //document.getElementById("pass1").style.borderColor = "#E34234";
 		         document.getElementById("pass2").style.borderColor = "#E34234";
 		         flag=false;
 		          }
   			 }
 		 
         // alert(flag);
          return flag;
          
	});
       
});    
   


