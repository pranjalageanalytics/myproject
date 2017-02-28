$(document).ready(function(){
$('.ckeckm').change(function() {
		  //$("#menu1").css("background","light");
		  		  
		  $("#menu1").css("background","white");
		  $("div.select1").replaceWith("Category Selected");
		 
		  console.log("sss");
		    });
	
	$('.local').change(function() {
		  //$("#menu1").css("background","light");
		  
		  
		  $("#menu2").css("background","white");
		  $("div.select2").replaceWith("Location selected");
		 
		  console.log("location");
		    });


 
	$("#sub").click(function(){
		flag = true;
		var date1 = document.getElementById("start_date").value;
		var date2 = document.getElementById("end_date").value;
		var date3 = document.getElementById("exp_date").value;
		var title = document.getElementById("title").value;
		var requested_volunteers = document.getElementById("requested_volunteers").value;
		var number = document.getElementById("number").value;
		var timepicker = document.getElementById("timepicker").value;
 	        var timepicker1 = document.getElementById("timepicker1").value;
		var venue = document.getElementById("venue").value;

		if(timepicker==""){
   
   $("#errortime").show();
   
      document.getElementById('errortime').innerHTML=" This field is required!";
      document.getElementById("timepicker").style.borderColor = "#E34234";

      flag=false;
      
     }
   else{
                         //flag=true;
     //alert("else of email")
                     $("#errortime").hide();
             
                       document.getElementById("timepicker").style.borderColor = "#ccc";
                    }
  
     if(timepicker1==""){
   
   $("#errortime1").show();
   
      document.getElementById('errortime1').innerHTML=" This field is required!";
      document.getElementById("timepicker1").style.borderColor = "#E34234";

      flag=false;
      
     }
   else{
                         //flag=true;
     //alert("else of email")
                     $("#errortime1").hide();
             
                       document.getElementById("timepicker1").style.borderColor = "#ccc";
                    }
		if(venue==""){
			
			$("#errorvenue").show();
			
			   document.getElementById('errorvenue').innerHTML=" This field is required!";
			   document.getElementById("venue").style.borderColor = "#E34234";

			   flag=false;
			   
			  }
		 else{
                         //flag=true;
  			//alert("else of email")
                     $("#errorvenue").hide();
             
                       document.getElementById("venue").style.borderColor = "#ccc";
                    }
		

		
		if(title==""){
			$("#errortitle").show();
			
			   document.getElementById('errortitle').innerHTML=" This field is required!";
			   document.getElementById("title").style.borderColor = "#E34234";

			   flag=false;
			   
			  }
		 else{
                        //flag=true;
  			//alert("else of email")
                        $("#errortitle").hide();
             
                        document.getElementById("title").style.borderColor = "#ccc";
                      }
		
		if(requested_volunteers=="")
		{
			         
               $("#errorvolunteer").show();
			
			   document.getElementById('errorvolunteer').innerHTML=" This field is required!";
		       document.getElementById("requested_volunteers").style.borderColor = "#E34234";

			   flag=false;
			   
		}
	     
		else{
                        //flag=true;
 			//alert("else of email")
                        $("#errorvolunteer").hide();
            
              document.getElementById("requested_volunteers").style.borderColor = "#ccc";
            }
		 var re =/^[0-9]*$/;
   	     if(requested_volunteers!=""){
             if(!re.test(requested_volunteers)) {
            
              $("#errorvolunteer").show();
            document.getElementById('errorvolunteer').innerHTML="Requested volunteer contains only digits";
            document.getElementById("requested_volunteers").style.borderColor = "#E34234";
             flag=false;
          
            
                 }
   	      }
		
		var d=new Date();
		var today = (d.getFullYear()+"-"+((d.getMonth()<10)?"0"+(d.getMonth()+1):(d.getMonth()+1))+"-"+((d.getDate()<10)?"0"+d.getDate():d.getDate()));
		console.log("today : ",today)
                //alert("today"+today);
		console.log(new Date(date1).getTime()-new Date(today).getTime())
                //alert("date1"+date1);
		if(date1==""){
			$("#errorstart").show();
			
			   document.getElementById('errorstart').innerHTML=" This field is required!";
				document.getElementById("start_date").style.borderColor = "#E34234";

			   flag=false;
			   
			  }
	
	
		else if (Date.parse(date1) > Date.parse(today)) {
			  

			   //flag=true;
			   $("#errorstart").hide();
	            
	           document.getElementById("start_date").style.borderColor = "#ccc"; 
			}
		
		
		else{
            //flag=true;
 			//alert("else of email")
           
                      // alert ("date is greater than today")
			   $("#errorstart").show();
				
			   document.getElementById('errorstart').innerHTML=" Start date is greater than today";
				document.getElementById("start_date").style.borderColor = "#E34234";
                       flag=false;
            }

                //alert("date2"+date2);
		
		if(date2==""){
			 //alert("hhhh")
			$("#errorend").show();
			
			   document.getElementById('errorend').innerHTML=" This field is required!";
				document.getElementById("end_date").style.borderColor = "#E34234";

			   flag=false;
			   
			  }
		else if(date2<date1){
			 //alert("exp date less than start date");
			    $("#errorend").show();
			    document.getElementById('errorend').innerHTML=" To date can't be less than start date!";
			    document.getElementById("end_date").style.borderColor = "#E34234";
			     flag=false;
			    }
		
		else{
		            //flag=true;
 			//alert("else of email")
 		           $("#errorend").hide();
            
              		document.getElementById("end_date").style.borderColor = "#ccc";
            	}
		 
		
		
		
		//alert("date3"+date3);
		if(date3==""){
			$("#errorexp").show();
			
			   document.getElementById('errorexp').innerHTML=" This field is required!";
				document.getElementById("exp_date").style.borderColor = "#E34234";

			   flag=false;
			   
			  }
		else if(date3>date2){
			// alert("exp date greater than end date");
			    $("#errorexp").show();
			    document.getElementById('errorexp').innerHTML=" Exp date can't be greater than end date!";
			    document.getElementById("exp_date").style.borderColor = "#E34234";
			     flag=false;
			    }
		 else if(Date.parse(date3)<Date.parse(today)){
			// alert("exp date less than start date");
			    $("#errorexp").show();
			    document.getElementById('errorexp').innerHTML=" Exp date can't be less than today date!";
			    document.getElementById("exp_date").style.borderColor = "#E34234";
			     flag=false;
			    }
		 else{
	            //flag=true;
	 			//alert("else of email")
	            $("#errorexp").hide();
	            
	              document.getElementById("exp_date").style.borderColor = "#ccc";
	            }
		 
		 
		 
        	  if(number==""){
        			$("#error1").show();
        			//alert("in contact")
        			   document.getElementById('error1').innerHTML=" This field is required!";
        				document.getElementById("number").style.borderColor = "#E34234";

        			   flag=false;
        			   
        			  }
        	  else{
                  //flag=true;
       			//alert("else of email")
                  $("#error1").hide();
                  
                    document.getElementById("number").style.borderColor = "#ccc";
                  }
        	  
        	  var re =/^[- +()]*[0-9][- +()0-9]*$/;
        	  if(number!=""){
                  if(!re.test(number)) {
                 
                   $("#error1").show();
                 document.getElementById('error1').innerHTML="Contact number contains only digits";
                 document.getElementById("number").style.borderColor = "#E34234";
                flag=false;
               
                 
                      }
                  if(number.length!=12)
                  {
                      //alert("in length");
                      $("#error1").show();
                    document.getElementById('error1').innerHTML="Contact number must be 12 digits";
                    document.getElementById("number").style.borderColor = "#E34234";
                   flag=false;
                   	
                    
                         }
        	  }
      		    
        	  
        	  
                 
        
          
        //  alert(flag);
          if (flag == false)
          {
        	  
        	  
          }
       else{
	
	
	
	allValues=[];
	allValues1=[];
	//$("#sub").click(function(e){
		//alert('within form submit');
		//allValues=[]
		var checkboxes=$("input:checkbox[name=location]");
	     console.log(checkboxes); 
	     for (var i = 0; i < checkboxes.length; i++)
	        {
	            if(checkboxes[i].checked==true)
	            	{
	            		console.log('k',checkboxes[i].value);
	            		allValues.push(checkboxes[i].value);
	            		
	            	}
	        }	
		//var state = $("#iframe").contents().find(":checkbox").is(":checked");
	     
	     console.log('checkboxes',allValues);
	     
	     if(allValues.length==0)
	    	 {
	    	 	//alert('please select locations')
	    	 	$("#errorlocation").show();
				
				   document.getElementById('errorlocation').innerHTML=" This field is required!";
				   document.getElementById("location").style.borderColor = "#E34234";

				   flag=false;
				   
	    	 	
	    	 }
	     
	     else
	     {
	    	 
	    	 $("#errorlocation").hide();
             
             document.getElementById("location").style.borderColor = "#ccc";  
	    	 
	     }
	     var checkboxes1=$("input:checkbox[name=category]");
	     console.log(checkboxes1); 
	     for (var i = 0; i < checkboxes1.length; i++)
	        {
	            if(checkboxes1[i].checked==true)
	            	{
	            		console.log('k',checkboxes1[i].value);
	            		allValues1.push(checkboxes1[i].value);
	            		
	            	}
	        }
	     if(allValues1.length==0)
    	 {
    	 	//alert('please select categories')
    		$("#errorcategory").show();
			
			   document.getElementById('errorcategory').innerHTML=" This field is required!";
			   document.getElementById("category").style.borderColor = "#E34234";

			   flag=false;
    	 }
	     else
	    	 {
	    	 	$("#errorcategory").hide();
             
             document.getElementById("category").style.borderColor = "#ccc";  
	    	 
	    	 }
		//var state = $("#iframe").contents().find(":checkbox").is(":checked");
	     
	     console.log('checkboxes',allValues1);
	   
	     var title=$("#title").val();
	     //console.log(title);
	     var start_date=$("#start_date").val();
	     //console.log(start_date);
	     var end_date=$("#end_date").val();
	     //console.log(end_date);
	     var reg_expire_date=$("#exp_date").val();
	     //console.log(reg_expire_date);
	     var start_time=$("#timepicker").val();
	     //console.log(start_time);
	     var end_time=$("#timepicker1").val();
	     //console.log(end_time);
	     var description=$("#description").val();
	     //console.log(description);
	     var requested_volunteers=$("#requested_volunteers").val();
	     //console.log(requested_volunteers);
	     var contact_no=$("#number").val();
	     //console.log(contact_no);
	     var venue=$("#venue").val();
	     //console.log(venue);
	     var direction=$("#direction").val();
	     //console.log(direction);
	     var photo= $("#image").val();

	     //console.log(photo);
	   

	     if(allValues1.length>0 && allValues.length>0)
	     {
		 $.ajax({
		   url : '/home/create_challenge/',
		   type : "POST",
		   enctype: 'multipart/form-data',
		   media_type:"photo",
		   data : {'allValues':allValues ,'allValues1':allValues1, 'title':title, 'start_date':start_date, 'end_date':end_date,
			       'reg_expire_date':reg_expire_date,'start_time':start_time, 'end_time':end_time, 'description':description,
			       'requested_volunteers':requested_volunteers,'contact_no':contact_no, 'venue':venue, 'direction':direction,
			       'photo':photo,
			       },
		   //dataType: 'json',
		   traditional: true,

            })
		
	     .done(function(data) {
             console.log("within sucess");
             $.each(data,function(key ,value){
                   console.log(value);
                   if(value=='error')
                    {
                     console.log('eroor has occured');
                     window.location.href="http://192.168.1.129:8063/home/pagenotfound/";
                    }
                   if(value=='success')
                    {
                      	$('#picture_form').submit();
                    console.log('success');
                    //window.location.href="http://192.168.1.129:8063/home/host_challenges/";
                    }
             });
             
             
        });
	 
          }
       
          else{
        	  //alert('Category & location can not null');
          }
       }   return flag;
       
	});
	
	
});

