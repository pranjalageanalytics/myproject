
$(document).ready(function(){
	$("#gifter_update").click(function(){
		flag = true;
		
		if($('input[name=gender]:checked').length<=0)
        {
        	 document.getElementById('error5').innerHTML=" This field is required!";
				//document.getElementById("website").style.borderColor = "#E34234";

			   flag=false;
        }
		
		if(datepicker.value=="") {
  			$("#dob_error").show();
  			
  			   document.getElementById('dob_error').innerHTML=" This field is required!";
  				document.getElementById("datepicker").style.borderColor = "#E34234";

  			   flag=false;
		}
		
		else if(datepicker.value!=""){ 
		
			if(datepicker.value.length!=10)
          {
          //alert("in length");
          $("#dob_error").show();
        document.getElementById('dob_error').innerHTML="Please Select Date of Birth";
        document.getElementById("datepicker").style.borderColor = "#E34234";
       flag=false;
       	//alert("in email if "+flag);
        
          }
		}		
		 else{
          
             $("#dob_error").hide();
             
               document.getElementById("datepicker").style.borderColor = "#ccc";
             }
   	  
        	  if(contact.value ==""){
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
        	  
        	  var re =/^[0-9]*$/;
        	  if(contact.value!=""){
                  if(!re.test(contact.value))
                  {
                 
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
      		    
                 
         // alert(flag);
            $('#profile_pic').submit();

          return flag;
          
	});
       
});    
   


