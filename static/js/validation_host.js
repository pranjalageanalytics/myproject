
$(document).ready(function(){
	$("#sub").click(function(){
		flag = true;
		 
        if(host_name.value==""){
  			$("#err4").show();
  			
  			   document.getElementById('err4').innerHTML=" This field is required!";
  				document.getElementById("host_name").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
        
        else{
			 
			 $("#err4").hide();
			 document.getElementById("host_name").style.borderColor = "#ccc";
		     }

          if(datepicker1.value==""){
  			$("#date2").show();
  			
  			   document.getElementById('date2').innerHTML=" This field is required!";
  				document.getElementById("datepicker1").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
           
          else{
              
              $("#date2").hide();
              
                document.getElementById("datepicker1").style.borderColor = "#ccc";
              }
          
        if(website.value==""){
  			$("#err5").show();
  			
  			   document.getElementById('err5').innerHTML=" This field is required!";
  				document.getElementById("website").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
        
        else{
            
            $("#err5").hide();
            
              document.getElementById("website").style.borderColor = "#ccc";
            } 
        
        if($('input[name=gender]:checked').length<=0)
        {
        	 document.getElementById('err8').innerHTML=" This field is required!";
				//document.getElementById("website").style.borderColor = "#E34234";

			   flag=false;
        }
        
        else{
			 
			 $("#err8").hide();
		   
		     }
        
		if(email1.value==""){
  			$("#err1").show();
  			
  			   document.getElementById('err1').innerHTML=" This field is required!";
  				document.getElementById("email1").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
          
          var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
          
          if(email1.value!=""){
              if(reg.test(email1.value) == false) {
             
               $("#err1").show();
             document.getElementById('err1').innerHTML="Invalid Email";
             document.getElementById("email1").style.borderColor = "#E34234";
            flag=false;
            	//alert("in email if "+flag);
             
                  }
           
  		    else{
             //flag=true;
  			//alert("else of email")
             $("#err1").hide();
               document.getElementById("email1").style.borderColor = "#ccc";
              
             }
             }
          
        	  if(contact1.value==""){
        			$("#err2").show();
        			//alert("in contact")
        			   document.getElementById('err2').innerHTML=" This field is required!";
        				document.getElementById("contact1").style.borderColor = "#E34234";

        			   flag=false;
        			   
        			  }
        	  else{
                  //flag=true;
       			//alert("else of email")
                  $("#err2").hide();
                  
                    document.getElementById("contact1").style.borderColor = "#ccc";
                  }
        	  
        	  var re =/^[- +()]*[0-9][- +()0-9]*$/;
        	  if(contact1.value!=""){
                  if(!re.test(contact1.value)) {
                 
                   $("#err2").show();
                 document.getElementById('err2').innerHTML="Contact number contains only digits";
                 document.getElementById("contact1").style.borderColor = "#E34234";
                flag=false;
                	//alert("in email if "+flag);
                 
                      }
                  if(contact1.value.length!=12)
                  {
                      //alert("in length");
                      $("#err2").show();
                    document.getElementById('err2').innerHTML="Contact number must be 12 digits";
                    document.getElementById("contact1").style.borderColor = "#E34234";
                   flag=false;
                   	//alert("in email if "+flag);
                    
                         }
        	  }
      		    
                 
        
        if(password1.value==""){
   		   document.getElementById('err6').innerHTML=" This field is required!";
   		   document.getElementById("password1").style.borderColor = "#E34234";

   		   flag=false;
   		   //alert(password1.value);
   		   }
        
   		  if(password1.value != "") {
   		   
   		         if(password1.value.length < 8) {
   		          console.log("length is less");
   		     document.getElementById('err6').innerHTML=" Password must contain at least Eight characters!";
   		     document.getElementById("password1").style.borderColor = "#E34234";
   		       // document.getElementById("pass2").style.borderColor = "#E34234";
   		           
   		           flag=false;
   		         }
   		         
   		         
   		         else if(!(re = /[0-9]/).test(password1.value)) {
   		          console.log("Number");
   		        document.getElementById('err6').innerHTML=" password must contain at least one number (0-9)!";
   		     document.getElementById("pwd").style.borderColor = "#E34234";
   		     //document.getElementById("pass2").style.borderColor = "#E34234";
   		           
   		           flag=false;
   		         }
   		         
   		         else if(!(re = /[a-z]/).test(password1.value)) {
   		          console.log("lowercase");
   		        document.getElementById('err6').innerHTML=" password must contain at least one lowercase letter (a-z)!";
   		     document.getElementById("pwd").style.borderColor = "#E34234";
   		           
   		           flag=false;
   		         }
   		         
   		         else if(!(re = /[A-Z]/).test(password1.value)) {
   		          console.log("uppercase");
   		     document.getElementById('err6').innerHTML=" password must contain at least one uppercase letter (A-Z)!";
   		     document.getElementById("password1").style.borderColor = "#E34234";
   		           
   		           flag=false;
   		         }
   		         else if(!(re = /[_\-!\"@;,.:]/).test(password1.value)) {
   		          console.log("special char");
   		     document.getElementById('err6').innerHTML=" password must contain at least one special character!";
   		     document.getElementById("password1").style.borderColor = "#E34234";
   		           
   		           flag=false;
   		         }
   		         else
   		          {
   		          document.getElementById('err6').innerHTML=" ";
   		          document.getElementById("password1").style.borderColor = "#ccc";
   		          }
   		       }
   		 if(password2.value==""){
   			 //alert("password2")
 		    document.getElementById('err7').innerHTML=" This field is required!";
 		         document.getElementById("password2").style.borderColor = "#E34234";

 		    flag=false;
 		    //alert(pass2.value);
 		    }
   		 else
		     {
		   document.getElementById('err7').innerHTML=" ";
		   document.getElementById("password2").style.borderColor = "#ccc";
		     }
   		 if (password2.value!="")
   			 {
   			 
   			
 		  if (password2.value!=password1.value) {
 		         
 		         document.getElementById('err7').innerHTML=" Password and confirm password must be same!";
 		         //document.getElementById("pass1").style.borderColor = "#E34234";
 		         document.getElementById("password2").style.borderColor = "#E34234";
 		         flag=false;
 		          }
   			 }
 		
          //alert(flag);
          return flag;
          
	});
       
});    
   


