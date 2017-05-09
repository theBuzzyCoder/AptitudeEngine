var data = undefined;
var state = "home";
var question_id = undefined;
var question = undefined;
var clickedOn = undefined;
function get_data(url,callback){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = callback;
  xhttp.open("GET",url, true);
  xhttp.send()
}
function post_data(url,callback,param){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = callback;
  xhttp.open("POST",url, true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(param);
}
function errorPage(errorMessage){
    state = "error";
  changeHeader();
  var intro = document.getElementById('intro');
  var sHeader = document.getElementById('s-header');
  var container = document.getElementById('container');
  var category = document.getElementById('category');
  var faq = document.getElementById('faq');
  var vq = document.getElementById('view-questions');
  var how = document.getElementById('how');
  var error = document.getElementById('error');
  var errorM = document.getElementById('error-message');
  var feedbackContainer = document.getElementById('feedback-container');
  feedbackContainer.style.display = "block";
  intro.style.display ="none";
  sHeader.style.display = "block";
  container.style.display = "none";
  category.style.display = "none";
  faq.style.display = "none";
  vq.style.display = "none";
  how.style.display = "none";
  error.style.display = "block";
  if(errorMessage != undefined)
  errorM.innerHTML = errorMessage;
  location.hash = state;
}
function loadHome(){
  state = "home";
  document.getElementById("first").innerHTML = "General";
  document.getElementById("second").innerHTML = "New Feature";
  document.getElementById("rd1").value = "1";
  document.getElementById("rd2").value = "2";
  location.hash = state;
  changeHeader();
  var intro = document.getElementById('intro');
  var sHeader = document.getElementById('s-header');
  var container = document.getElementById('container');
  var category = document.getElementById('category');
  var faq = document.getElementById('faq');
  var vq = document.getElementById('view-questions');
  var how = document.getElementById('how');
  var error = document.getElementById('error');
  var feedbackContainer = document.getElementById('feedback-container');
  feedbackContainer.style.display = "none";
  intro.style.display ="block";
  sHeader.style.display = "block";
  container.style.display = "none";
  category.style.display = "none";
  faq.style.display = "none";
  vq.style.display = "none";
  how.style.display = "none";
  error.style.display = "none";
}
function categoryClick(e){
  var url;
 if(this.childNodes != undefined)
 url = "http://"+location.host+"/questions/"+this.childNodes[1].innerHTML;
 else url = "http://"+location.host+"/questions/"+clickedOn;
 showLoader();
 get_data(url,view_questions);
}
function questionClick()
{
  var edit = document.getElementById('ques');
  edit.value = this.innerHTML;
  load_question();
}
function view_questions()
{
  document.getElementById("first").innerHTML = "General";
  document.getElementById("second").innerHTML = "New Feature";
  document.getElementById("rd1").value = "1";
  document.getElementById("rd2").value = "2";
  document.body.scrollTop = document.documentElement.scrollTop = 0;
  if(this.readyState == 4 && this.status == 200)
  {
    state = "viewQuestions";
    data = JSON.parse(this.response);
    changeHeader();
    var intro = document.getElementById('intro');
    var sHeader = document.getElementById('s-header');
    var container = document.getElementById('container');
    var category = document.getElementById('category');
    var faq = document.getElementById('faq');
    var vq = document.getElementById('view-questions');
    var how = document.getElementById('how');
    var error = document.getElementById('error');
    intro.style.display ="none";
    sHeader.style.display = "none";
    container.style.display = "none";
    category.style.display = "none";
    faq.style.display = "none";
    vq.style.display = "block";
    how.style.display = "none";
    error.style.display = "none";
    vq.innerHTML = "";
    for(var index in data){
      var div = document.createElement("DIV");
      div.innerHTML = data[index];
      div.className = "card v-question";
      div.addEventListener('click',questionClick,false);
      vq.appendChild(div);
    }
    location.hash = state;
  }else if (status == 404 || status == 500)
  errorPage("There seems to be some problem contacting the server please try after some time.");
  closeLoader();
  document.body.scrollTop = document.documentElement.scrollTop = 0;
}
function catPage(){
  document.getElementById("first").innerHTML = "General";
  document.getElementById("second").innerHTML = "New Feature";
  document.getElementById("rd1").value = "1";
  document.getElementById("rd2").value = "2";
  state = "category";
  location.hash = state;
  var call = function(){
    if (this.readyState == 4 && this.status == 200) {
      var data = JSON.parse(this.response);
      var intro = document.getElementById('intro');
      var sHeader = document.getElementById('s-header');
      var container = document.getElementById('container');
      var category = document.getElementById('category');
      var faq = document.getElementById('faq');
      var vq = document.getElementById('view-questions');
      var how = document.getElementById('how');
      var error = document.getElementById('error');
      var colors = ["#2196f3","#c0ca33","#ff9800","#0cc69b"];
      var feedbackContainer = document.getElementById('feedback-container');
      feedbackContainer.style.display = "block";
      intro.style.display ="none";
      sHeader.style.display = "none";
      container.style.display = "none";
      category.style.display = "block";
      faq.style.display = "none";
      vq.style.display = "none";
      how.style.display = "none";
      error.style.display = "none";
      category.innerHTML = "";
      var i=0;
      for (item in data){
        var cat = createModule(data[item]['name'],data[item]['image'],colors[i++ % colors.length]);
        cat.addEventListener('click',categoryClick,false);
        category.appendChild(cat);
      }
    }else if (status == 404 || status == 500)
    errorPage("There seems to be some problem contacting the server please try after some time.");
    closeLoader();
    document.body.scrollTop = document.documentElement.scrollTop = 0;
  }
  var url = "http://"+location.host+"/modules";
  get_data(url,call);
  showLoader();
}
function createModule(module,image,color){
  var mod = document.createElement('DIV');
  mod.className = "card cat";
  var img = document.createElement('IMG');
  img.src = image;
  var title = document.createElement('DIV');
  title.className = "cat-title";
  title.style.backgroundColor = color;
  var text = document.createTextNode(module);
  title.appendChild(text);
  mod.appendChild(img);
  mod.appendChild(title);
  return mod;
}
function faqPage(){
  state = "faq";
  location.hash = state;
  document.getElementById("first").innerHTML = "General";
  document.getElementById("second").innerHTML = "New Feature";
  document.getElementById("rd1").value = "1";
  document.getElementById("rd2").value = "2";
  changeHeader();
  var intro = document.getElementById('intro');
  var sHeader = document.getElementById('s-header');
  var container = document.getElementById('container');
  var category = document.getElementById('category');
  var faq = document.getElementById('faq');
  var vq = document.getElementById('view-questions');
  var how = document.getElementById('how');
  var error = document.getElementById('error');
  var feedbackContainer = document.getElementById('feedback-container');
  feedbackContainer.style.display = "block";
  intro.style.display ="none";
  sHeader.style.display = "none";
  container.style.display = "none";
  category.style.display = "none";
  faq.style.display = "block";
  vq.style.display = "none";
  how.style.display = "none";
  error.style.display = "none";
}
function howPage()
{
  document.getElementById("first").innerHTML = "General";
  document.getElementById("second").innerHTML = "New Feature";
  document.getElementById("rd1").value = "1";
  document.getElementById("rd2").value = "2";
  state = "how";
  location.hash = state;
  changeHeader();
  var intro = document.getElementById('intro');
  var sHeader = document.getElementById('s-header');
  var container = document.getElementById('container');
  var category = document.getElementById('category');
  var faq = document.getElementById('faq');
  var vq = document.getElementById('view-questions');
  var how = document.getElementById('how');
  var error = document.getElementById('error');
  var feedbackContainer = document.getElementById('feedback-container');
  feedbackContainer.style.display = "block";
  intro.style.display ="none";
  sHeader.style.display = "none";
  container.style.display = "none";
  category.style.display = "none";
  faq.style.display = "none";
  vq.style.display = "none";
  how.style.display = "block";
  error.style.display = "none";
}
function updateSolutionView(data)
{
  var edit = document.getElementById('ques');
  document.getElementById("first").innerHTML = "Wrong answer";
  document.getElementById("second").innerHTML = "Failed to solve";
  document.getElementById("rd1").value = "3";
    document.getElementById("rd2").value = "4";
  if(!('error' in data))
  {
    state ="question";
    location.hash = state;
    console.log("called");
    changeHeader();
    var sol = document.getElementById('sol');
    var question = document.getElementById('question');
    var rel = document.getElementById('rel');
    var intro = document.getElementById('intro');
    var container = document.getElementById('container');
    var error = document.getElementById('error');
    var vq = document.getElementById('view-questions');
    var sHeader = document.getElementById('s-header');
    var feedbackContainer = document.getElementById('feedback-container');
    sHeader.style.display = "block";
    feedbackContainer.style.display = "block";
    vq.style.display = "none";
    error.style.display = "none";
    container.style.display = "block";
    intro.style.display ="none";
    sol.style.display ="inline-block";
    rel.style.display ="inline-block";
    rel.style.height = sol.clientHeight-30 +"px";
    question.innerHTML = edit.value;
    var result = document.getElementById('result');
    var cont = document.getElementById('sol-container');
    cont.innerHTML = "";
    rel.innerHTML = '<span id ="rel-text"> Related Questions </span>';
    var related = data.related;
    var solution = data.solution;
    question_id = solution.id;
    result.innerHTML = solution.result;
    var steps = solution.steps
    document.getElementById('q-type').innerHTML = solution.type +" > "+solution.stype;
    for(index in steps)
    {
      var card = document.createElement("DIV");
      card.className ="card step";
      var step =  document.createElement("DIV");
      step.className ="step-no color"+(index%5+1);
      step.style.verticalAlign = "middle";
      step.appendChild(document.createTextNode(parseInt(index)+1));
      card.appendChild(step);
      cont.appendChild(card);
      var div = document.createElement("DIV");
      div.style.display = "inline-block";
      div.style.fontSize = "14px";
      var w = card.clientWidth - step.clientWidth - 45;
      div.style.width = w + "px";
      div.style.verticalAlign = "middle";
      steps[index] = steps[index].replace(new RegExp('\n', 'g'), '<br/>')
      div.innerHTML = steps[index];
      card.appendChild(div);
    }
    for(question in related)
    {
      var div = document.createElement("DIV");
      div.className = "rel-ques";
      div.addEventListener('click',relatedClick,false);
      div.innerHTML = related[question];
      rel.appendChild(div);
    }
  }  else errorPage(data.error);
}
function relatedClick(){
  var edit = document.getElementById('ques');
  edit.value = this.innerHTML;
  load_question();
}
function load_question() {
    var edit = document.getElementById('ques');
    if(edit.value != "" && edit.value.length >5){
      var callback = function() {
          if (this.readyState == 4 && this.status == 200) {
              console.log(this.response);
              data = JSON.parse(this.response);
              question = edit.value;
              updateSolutionView(data);
            }else if (status == 404 || status == 500)
            errorPage("There seems to be some problem contacting the server please try after some time.");
            closeLoader();
            document.body.scrollTop = document.documentElement.scrollTop = 0;
      };
      if(question == edit.value)
      updateSolutionView(data);
      else{
        var url = "http://"+location.host+"/solve";
        param = "question=" + edit.value;
        post_data(url,callback,param);
        showLoader();
      }
    }else alert("Please enter a valid question");
}
function handleKeyPress(e)
{
  if(e.keyCode == 13)
  {
    load_question();
  }
}
window.onresize = function(){
  changeHeader();
  if(state == "question")
  load_question();
};
window.onhashchange = function(){
  switch(location.hash){
    case "#home":loadHome();
                break;
    case "#category":catPage();
                break;
    case "#error":errorPage();
                break;
    case "#question":load_question();
                break;
    case "#faq":faqPage();
                break;
    case "#how":howPage();
                break;
    case "#viewQuestions": break;
    default: loadHome();
  }
};

function changeHeader()
{
  var edit = document.getElementById('ques');
  if(state != "home")
  {
    document.body.style.paddingTop = "0px";
    var logo = document.getElementById('logo');
    var ques = document.getElementById('ques-wrap');
    var w;

    if((w=document.body.clientWidth - logo.clientWidth) > 400 ){
      logo.style.display ="none"
      if(logo.clientHeight > 100)
    ques.style.paddingTop = "40px";
    else ques.style.paddingTop = "20px";
    //logo.style.display = "inline-block";
    ques.style.display = "block";
    ques.style.width = document.body.clientWidth +"px";
    ques.style.verticalAlign ="top";
    //logo.style.marginLeft = "0px";
    //logo.style.marginRight = "0px";
    w-=100;
    edit.style.width = (ques.clientWidth-400)+"px";
    ques.paddingTop ="5px";
  }else{
    logo.style.display = "block";
    ques.style.display = "block";
    ques.style.paddingTop = "2px";
    w = document.body.clientWidth-15;
    ques.style.width =w+"px";
    edit.style.width =w-document.getElementById('solve').clientWidth-35+"px";
  }
}else{
  var logo = document.getElementById('logo');
  logo.style.display = "block";
  var edit = document.getElementById('ques');
  edit.style.width = "60%";
}
}
function showLoader()
{
  document.getElementById('loader-container').style.display = "block";
}
function closeLoader()
{
  document.getElementById('loader-container').style.display = "none";
}
var feedbackSubmit = function(){
  var text = document.getElementById('feedback').value;
  text = text.trim();
  if(text != "")
  {
    var val1 = document.getElementById('rd1').value;
    var val2 = document.getElementById('rd2').value;
    var val;
    if(document.getElementById('rd1'))
    val = parseInt(val1);
    else val = parseInt(val2);
    var data = {};

    if(val1 == "3")
    data['id'] = question_id;
    else data['id'] = 0;
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    name = name.trim();
    email = email.trim();
    if(name == "" || email == ""){
    alert("Please Enter your name or email")
    return
    }
    var regexp = /^[a-z0-9.]+@[a-z0-9]+\.[a-z]+$/i;
    if(!regexp.test(email))
    {
      alert("Invalid Email");
      return;
    }
    data['name'] = name;
    data['type'] = val;
    data['email'] = email;
    data['ftext'] = text;
    showLoader();
    post_data("http://"+location.host+"/feedback",afterFeedback,"data="+JSON.stringify(data));
  }else alert("Please enter your feedback");
};
function afterFeedback()
{
  closeLoader();
  if(this.readyState == 4 && this.status == 200)
  alert("Feedback submission successfull");
}
