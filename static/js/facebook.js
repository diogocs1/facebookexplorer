// $(function(){
//   window.fbAsyncInit = function() {
//     FB.init({
//       appId      : '573216906148994',
//       // cookie     : true,
//       xfbml      : true,
//       version    : 'v2.0'
//     });

//     FB.getLoginStatus(function(response){
//       if (response.status === 'connected'){
//         token = response.authResponse.accessToken;
//         console.log(token);
//         window.location = "http://localhost:5000/home?token=" + token;
//       }else if (response.status === 'not_authorized'){
//         console.log(response);
//       }
//     });
//   };

//   (function(d, s, id){
//      var js, fjs = d.getElementsByTagName(s)[0];
//      if (d.getElementById(id)) {return;}
//      js = d.createElement(s); js.id = id;
//      js.src = "//connect.facebook.net/en_US/sdk.js";
//      fjs.parentNode.insertBefore(js, fjs);
//   }(document, 'script', 'facebook-jssdk'));

//   $("#login").click(function(){
//     FB.login(function(response){
//       console.log(response);
//     }, {scope : "public_profile", display : "dialog"});
//   });



// });

// https://www.facebook.com/dialog/oauth?client_id=573216906148994&redirect_uri=http://localhost:5000