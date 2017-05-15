$(document).ready(function(){
   console.log("in docu");
   $("#Addbooks").on('click', AddBooks);
   $("#issueBooks").on('click', IssuedBooks);
   $('#addStudent').on('click', studentRecord );
   $('#addTeacher').on('click', TeacherRecord );
   $('#book_search').DataTable();
   $('#st_record').DataTable();
   $('#t_record').DataTable();
   $('#is_books').DataTable();
   $('#book_search a').editable({
      type:'text',
      name:'book_name',
      url: '/updateBook',
      title:'Enter Book name',
      send:'always',
      pk:'1',
      ajaxOptions : {
           beforeSend: function(xhr, settings) {                                        
              if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                  //console.log("in before send ",settings);
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
            },
           type:'post',
           dataType: 'json',
           url:'/updateBook',
           //data: {book_name:$(this).editable('getValue')},
           success: function( data ) {
		console.log("data is",data);
           }                                                                            
      }


   })


   checkboxes = document.getElementsByTagName("input"); 

   for (var i = 0; i < checkboxes.length; i++) {
        var checkbox = checkboxes[i];
        checkbox.onclick = function(event) {
            var currentRow = this.parentNode.parentNode;
            var book_name = currentRow.getElementsByTagName("td")[0];
            var uid = currentRow.getElementsByTagName("td")[2];
        
            //alert("My text is: " + secondColumn.textContent );
            console.log("data is in uid bookname", book_name.textContent, uid.textContent);
            updateSubmission(book_name.textContent,uid.textContent);

          } 
   };

});

function getCookie(name) {
   var cookieValue = null;
   if (document.cookie && document.cookie != '') {
       var cookies = document.cookie.split(';');
       for (var i = 0; i < cookies.length; i++) {
           var cookie = jQuery.trim(cookies[i]);
           // Does this cookie string begin with the name we want?
           if (cookie.substring(0, name.length + 1) == (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
           }
       }
   }
   return cookieValue;
} 

var csrftoken = getCookie('csrftoken');    
function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
} 

function sameOrigin(url) {
   // test that a given url is a same-origin URL
   // url could be relative or scheme relative or absolute
   var host = document.location.host; // host + port
   var protocol = document.location.protocol;
   var sr_origin = '//' + host;
   var origin = protocol + sr_origin;
   // Allow absolute or scheme relative URLs to same origin
   return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
       (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
       // or any other URL that isn't scheme relative or absolute i.e relative.
       !(/^(\/\/|http:|https:).*/.test(url));
}

function updateSubmission(book_name, uid){
      //console.log("in update submission");
      $.ajax({                                                                                   
        beforeSend: function(xhr, settings) {                                        
           if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
               //console.log("in before send ",settings);
               xhr.setRequestHeader("X-CSRFToken", csrftoken);
           }
         },
         url: "/updateSubmission",
         type:'POST',
         dataType: 'json',
         data: {book_name:book_name, uid:uid},
         success: function( data ) {
          //console.log("data is", data);
          if (data.success === 0){
             window.location.reload();
             //console.log("updated book entry");
             var divToappend = '<div class="alert alert-success">' +
                  ' <a href="#" class="close" data-dismiss="alert"' + 
                  ' aria-label="close">&times;</a>' +
                  'Book entry updated</div>';
             $("#status").append($(divToappend));
          }else {
             var divToappend = '<div class="alert alert-danger">' +
                    ' <a href="#" class="close" data-dismiss="alert"' + 
                    ' aria-label="close">&times;</a>' +
                    'Something went wrong, Unable to update records</div>';
             $("#status").append($(divToappend));
           }
         },
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);        
        }
                                                                                         
      }); 

}


function AddBooks(event){
   event.preventDefault();
   //console.log("in add books 2 1");
   var book_name = $("#book_name").val();
   var authName = $("#authName").val();
   var dpt = $("#dpt").val();
   //console.log("data in client",book_name,authName,dpt);
   if ( !book_name || !authName || !dpt ){
      var divToappend = '<div class="alert alert-danger">' +
             ' <a href="#" class="close" data-dismiss="alert"' + 
             ' aria-label="close">&times;</a>' +
             'All field are required </div>';
      $("#status").append($(divToappend));

   }else{
       $.ajax({
         beforeSend: function(xhr, settings) {                                        
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                //console.log("in before send ",settings);
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
       },
       url: "/addBooks",
       type:'POST',
       dataType: 'json',
       data: {book_name:book_name, authname:authName, dpt:dpt},
       success: function( data ) {
        //console.log("data is", data);
        if (data.success === 0){
           window.location.reload();
        }
        var divToappend = '<div class="alert alert-success">' +
             ' <a href="#" class="close" data-dismiss="alert"' + 
             ' aria-label="close">&times;</a>' +
             'Book added successfully</div>';
        $("#status").append($(divToappend));
        //response( json );
       },
      error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText);        
      }

    }); 
  } 
}

function IssuedBooks(event){
    event.preventDefault();
    //console.log("in issued books ");
    var book_name = $("#book_name").val();
    var stName = $("#stName").val();
    var roll_no = $("#rnu").val();
    var from = $("#isdate").val();
    var to = $("#to").val()
    if ( !book_name || !stName || !roll_no || !isdate || !to ){
      var  divToappend = '<div class="alert alert-danger">' +
              ' <a href="#" class="close" data-dismiss="alert"' + 
              ' aria-label="close">&times;</a>' +
              'All field are required </div>';
       $("#status").append($(divToappend));
                                                                       
    }else{
      $.ajax({
        beforeSend: function(xhr, settings) {                                        
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                //console.log("in before send ",settings);
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        url: "/issbooks",
        type:'POST',
        dataType: 'json',
        data: {book_name:book_name, stname:stName, roll_no:roll_no, from:from, to:to},
        success: function(data) {
          //console.log("data is", data);
          if (data.success === 0){
            //console.log("reloading....");
            window.location.reload();
          }else{
             var divToappend = '<div class="alert alert-danger">' +
                    ' <a href="#" class="close" data-dismiss="alert"' + 
                    ' aria-label="close">&times;</a>' +
                    'Something went wrong, Please check student details or book Availability</div>';
             $("#status").append($(divToappend));
          }
        },
       error : function(xhr,errmsg,err) {
           console.log(xhr.status + ": " + xhr.responseText);        
       }
     }); 
    } 
}

function studentRecord(event){
    event.preventDefault();
    //console.log("in add student")
    var stuname = $("#stName").val();
    var uno = $("#uno").val();
    var dpt = $("#dpt").val();
    //var noOfIssBook = $("#noiss").val();
    //console.log("in stu record", stuname, uno, dpt)
    if ( !stuname || !uno || !dpt ){
       var divToappend = '<div class="alert alert-danger">' +
              ' <a href="#" class="close" data-dismiss="alert"' + 
              ' aria-label="close">&times;</a>' +
              'All field are required </div>';
       $("#status").append($(divToappend));
                                                                       
    }else{
      $.ajax({
        beforeSend: function(xhr, settings) {                                        
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                //console.log("in before send ",settings);
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        url: "/addStudent",
        type:'POST',
        dataType: "json",
        data: {stName:stuname, uno:uno, dpt:dpt},
        success: function( data) {
         //console.log("data is",data);
          if (data.success === 0){
            //console.log("reloading....");
            window.location.reload();
          }else {
             var divToappend = '<div class="alert alert-danger">' +
                    ' <a href="#" class="close" data-dismiss="alert"' + 
                    ' aria-label="close">&times;</a>' +
                    'Something went wrong, Record can not be updated</div>';
             $("#status").append($(divToappend));
          }
        },
       error : function(xhr,errmsg,err) {
           console.log(xhr.status + ": " + xhr.responseText);        
       }
     }); 
                                                                       
    } 
}                                                                  


function TeacherRecord(event){
    event.preventDefault();
    //console.log("in add Teacher")
    var tname = $("#tName").val();
    var eid = $("#eid").val();
    var tdpt = $("#tdpt").val();
    //console.log("in stu record", tname, eid, tdpt)
    if ( !tname || !eid || !tdpt ){
       var divToappend = '<div class="alert alert-danger">' +
              ' <a href="#" class="close" data-dismiss="alert"' + 
              ' aria-label="close">&times;</a>' +
              'All field are required </div>';
       $("#status").append($(divToappend));
                                                                       
    }else{
      $.ajax({
        beforeSend: function(xhr, settings) {                                        
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                //console.log("in before send ",settings);
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        url: "/addTeacher",
        type:'POST',
        dataType: "json",
        data: {tName:tname, eid:eid, tdpt:tdpt},
        success: function( data) {
         //console.log("data is",data);
          if (data.success === 0){
            //console.log("reloading....");
            window.location.reload();
          }else {
             var divToappend = '<div class="alert alert-danger">' +
                    ' <a href="#" class="close" data-dismiss="alert"' + 
                    ' aria-label="close">&times;</a>' +
                    'Something went wrong, Record can not be updated</div>';
             $("#status").append($(divToappend));
          }
        },
       error : function(xhr,errmsg,err) {
           console.log(xhr.status + ": " + xhr.responseText);        
       }
     }); 
                                                                       
    } 
}                                                                  
