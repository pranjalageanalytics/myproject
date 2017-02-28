$(document).ready(function(){
	
	
	
	$("#old_password").change(function(){
		
		var old_password = document.getElementById('old_password').value
		var new_password = document.getElementById('new_password').value
		var confirm_password = document.getElementById('confirm_password').value
		
		flag=true;
		console.log('on key up event of pass2');
		 if(old_password==""){
			 alert("kkkkkk");
				document.getElementById('errs').innerHTML=" This field is required!";
		    	  document.getElementById("old_password").style.borderColor = "#E34234";

				flag=false;
				//alert(pass2.value);
				}
		  if (old_password != "" && old_password == new_password) {
	           console.log("in old")
	    	   document.getElementById('errs').innerHTML="Old password & new passsword should not be same!";
	    	   //document.getElementById("pass1").style.borderColor = "#E34234";
	    	   document.getElementById("old_password").style.borderColor = "#E34234";
	    	   document.getElementById("rohi").style.visibility="hidden";
	    	   console.log( document.getElementById("rohi"))
	    	   flag=false;
	    	    }
		else
    	{
			document.getElementById('errs').innerHTML=" ";
			document.getElementById("old_password").style.borderColor = "#ccc";
    	}
		return flag;
});
	
	
	$("#confirm_password").change(function(){
		
		var old_password = document.getElementById('old_password').value
		var new_password = document.getElementById('new_password').value
		var confirm_password = document.getElementById('confirm_password').value
		
		flag=true;
		console.log('on key up event of pass2');
		 if(confirm_password==""){
				document.getElementById('qwerty').innerHTML=" This field is required!";
		    	  document.getElementById("confirm_password").style.borderColor = "#E34234";

				flag=false;
				//alert(pass2.value);
				}
		if (confirm_password!=new_password) {
	        
	    	   document.getElementById('qwerty').innerHTML=" Password and confirm password must be same!";
	    	   //document.getElementById("pass1").style.borderColor = "#E34234";
	    	   document.getElementById("confirm_password").style.borderColor = "#E34234";
	    	   flag=false;
	    	    }
		else
    	{
			document.getElementById('qwerty').innerHTML=" ";
			document.getElementById("confirm_password").style.borderColor = "#ccc";
    	}
		return flag;
});
	$("#new_password").change(function(){
		console.log('on key up event of pass1');
		var old_password = document.getElementById('old_password').value
		var new_password = document.getElementById('new_password').value
		var confirm_password = document.getElementById('confirm_password').value
		
		flag=true;
		if(new_password==""){
			document.getElementById('err1').innerHTML=" This field is required!";
	    	  document.getElementById("new_password").style.borderColor = "#E34234";

			flag=false;
			//alert(pass1.value);
			}
		if(new_password!= "") {
			
	        if(new_password.length < 8) {
	        	console.log("length is less");
	    document.getElementById('err1').innerHTML=" Password must contain at least Eight characters!";
	    document.getElementById("new_password").style.borderColor = "#E34234";
	      // document.getElementById("pass2").style.borderColor = "#E34234";
	          
	          flag=false;
	        }
	        
	        
	        else if(!(re = /[0-9]/).test(new_password)) {
	        	console.log("Number");
	       document.getElementById('err1').innerHTML=" password must contain at least one number (0-9)!";
	    document.getElementById("new_password").style.borderColor = "#E34234";
	    //document.getElementById("pass2").style.borderColor = "#E34234";
	          
	          flag=false;
	        }
	        
	        else if(!(re = /[a-z]/).test(new_password)) {
	        	console.log("lowercase");
	       document.getElementById('err1').innerHTML=" password must contain at least one lowercase letter (a-z)!";
	    document.getElementById("new_password").style.borderColor = "#E34234";
	          
	          flag=false;
	        }
	        
	        else if(!(re = /[A-Z]/).test(new_password)) {
	        	console.log("uppercase");
	    document.getElementById('error5').innerHTML=" password must contain at least one uppercase letter (A-Z)!";
	    document.getElementById("new_password").style.borderColor = "#E34234";
	          
	          flag=false;
	        }
	        else if(!(re = /[_\-!\"@;,.:]/).test(new_password)) {
	        	console.log("special char");
	    document.getElementById('err1').innerHTML=" password must contain at least one special character!";
	    document.getElementById("new_password").style.borderColor = "#E34234";
	          
	          flag=false;
	        }
	        else
	        	{
	        	document.getElementById('err1').innerHTML=" ";
	    	    document.getElementById("new_password").style.borderColor = "#ccc";
	        	}
	      }
	  
	    
return flag;

	});
	
	

$("#submit_frm").click(function() {
	console.log("submit form");
	flag=true;
	var old_password = document.getElementById('old_password').value
	var new_password = document.getElementById('new_password').value
	var confirm_password = document.getElementById('confirm_password').value
	
	 if(old_password==""){
		//alert("hiii");
			document.getElementById('errs').innerHTML=" This field is required!";
	    	  document.getElementById("old_password").style.borderColor = "#E34234";

			flag=false;
			
			}
	  if(new_password==""){
		// alert("hiii new pwd");
			document.getElementById('err1').innerHTML=" This field is required!";
	    	  document.getElementById("new_password").style.borderColor = "#E34234";

			flag=false;
			
			}
	  if(confirm_password==""){
		// alert("hiii confrm pwd");
				document.getElementById('qwerty').innerHTML=" This field is required!";
		    	  document.getElementById("confirm_password").style.borderColor = "#E34234";

				flag=false;
				
				}
	 
	 else if (old_password!= "" && old_password == new_password) {
        // alert("in old")
  	   document.getElementById('errs').innerHTML="Old password & new passsword should not be same!";
  	   //document.getElementById("pass1").style.borderColor = "#E34234";
  	   document.getElementById("old_password").style.borderColor = "#E34234";
  	 document.getElementById("rohi").style.visibility="hidden";
  	 console.log("rohi ",document.getElementById("rohi"))
  	   flag=false;
  	    }
	 else
	 	{
		 flag=true;
				document.getElementById('errs').innerHTML=" ";
				document.getElementById("old_password").style.borderColor = "#ccc";
	 	}
	
	 
		
		 console.log("value of flag : ",flag);
		 if(flag==true)
			 {
			 console.log("within true");
			 $('#login-form').submit()
			 }
});
});