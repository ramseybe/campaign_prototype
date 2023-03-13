from IPython.core.display import HTML
file = pd.read_csv('https://raw.githubusercontent.com/ramseybe/hackathon_campaign/main/50_toss_up1.csv')
file=file.drop(["Unnamed: 0"],axis=1)
def create_card(name):
    tempname=name.title()
    name=name.lower()
    person=file.iloc[file.index[file["name"] == tempname].values[0]]
    print(person)
    card="""<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>



<div class="card">
  <img src="person.jpeg" alt="person" style="width:100%">
  <h1>person</h1>
  <p class="title">district, party</p>
  <p>Harvard University</p>
  <div style="margin: 24px 0;">
    <a href="#"><i class="fa fa-venus"></i></a> 
    <a href="#"><i class="fa fa-reddit-alien"></i></a>  
    <a href="#"><i class="fa fa-linkedin"></i></a>  
    <a href="#"><i class="fa fa-facebook"></i></a> 
  </div>
  <p><button>Donate!</button></p>
</div>

</body>
</html>"""
    #name
    card=card.replace("person",name)
    #district
    card=card.replace("district",person["district"])
    #party
    card=card.replace("party",person["party"])
    return HTML(card)
  
create_card("williams")
