
$(document).ready(function(){
	$("#sub").click(function(){
		
		
		var host_name = document.getElementById("host_name").value
    	//alert(" value is -- " + host_name);
		
		var datepicker1 = document.getElementById("datepicker1").value
    	//alert(" value is -- " + datepicker1);
		
		var website = document.getElementById("website").value
    	//alert(" value is -- " + website);
		
		var email1 = document.getElementById("email1").value
    	//alert(" value is -- " + website);
		
		var contact1 = document.getElementById("contact1").value
    	//alert(" value is -- " + website);
		
		var password1 = document.getElementById("password1").value
    	//alert(" value is -- " + website);
		
		var password2 = document.getElementById("password2").value
    	//alert(" value is -- " + website);
		
		flag = true;
		 
        if(host_name==""){
  			$("#err4").show();
  			
  			   document.getElementById('err4').innerHTML=" This field is required!";
  				document.getElementById("host_name").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
        
        else{
			 
			 $("#err4").hide();
			 document.getElementById("host_name").style.borderColor = "#ccc";
		     }

          if(datepicker1==""){
  			$("#date2").show();
  			
  			   document.getElementById('date2').innerHTML=" This field is required!";
  				document.getElementById("datepicker1").style.borderColor = "#E34234";

  			   flag=false;
  			   
  			  }
           
          else{
              
              $("#date2").hide();
              
                document.getElementById("datepicker1").style.borderColor = "#ccc";
              }
          
          if(website==""){
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
          
          if(email1==""){
    			$("#err1").show();
    			
    			   document.getElementById('err1').innerHTML=" This field is required!";
    				document.getElementById("email1").style.borderColor = "#E34234";

    			   flag=false;
    			   
    			  }
            
            var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
            
            if(email1!=""){
                if(reg.test(email1) == false) {
               
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
            
            
            if(contact1==""){
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
    	  if(contact1!=""){
              if(!re.test(contact1)) {
             
               $("#err2").show();
             document.getElementById('err2').innerHTML="Contact number contains only digits";
             document.getElementById("contact1").style.borderColor = "#E34234";
            flag=false;
            	//alert("in email if "+flag);
             
                  }
              if(contact1.length!=12)
              {
                  //alert("in length");
                  $("#err2").show();
                document.getElementById('err2').innerHTML="Contact number must be 12 digits";
                document.getElementById("contact1").style.borderColor = "#E34234";
               flag=false;
               	//alert("in email if "+flag);
                
                     }
    	  }
  		    
          
    	  if(password1==""){
      		   document.getElementById('err6').innerHTML=" This field is required!";
      		   document.getElementById("password1").style.borderColor = "#E34234";

      		   flag=false;
      		   //alert(password1.value);
      		   }
           
      		  if(password1!= "") {
      		   
      		         if(password1.length < 8) {
      		          console.log("length is less");
      		     document.getElementById('err6').innerHTML=" Password must contain at least Eight characters!";
      		     document.getElementById("password1").style.borderColor = "#E34234";
      		       // document.getElementById("pass2").style.borderColor = "#E34234";
      		           
      		           flag=false;
      		         }
      		         
      		         
      		         else if(!(re = /[0-9]/).test(password1)) {
      		          console.log("Number");
      		        document.getElementById('err6').innerHTML=" password must contain at least one number (0-9)!";
      		     document.getElementById("pwd").style.borderColor = "#E34234";
      		     //document.getElementById("pass2").style.borderColor = "#E34234";
      		           
      		           flag=false;
      		         }
      		         
      		         else if(!(re = /[a-z]/).test(password1)) {
      		          console.log("lowercase");
      		        document.getElementById('err6').innerHTML=" password must contain at least one lowercase letter (a-z)!";
      		     document.getElementById("pwd").style.borderColor = "#E34234";
      		           
      		           flag=false;
      		         }
      		         
      		         else if(!(re = /[A-Z]/).test(password1)) {
      		          console.log("uppercase");
      		     document.getElementById('err6').innerHTML=" password must contain at least one uppercase letter (A-Z)!";
      		     document.getElementById("password1").style.borderColor = "#E34234";
      		           
      		           flag=false;
      		         }
      		         else if(!(re = /[_\-!\"@;,.:]/).test(password1)) {
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
      		  
      		  
      		 if(password2==""){
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
       		 if (password2!="")
       			 {
       			 
       			
     		  if (password2!=password1) {
     		         
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
   


