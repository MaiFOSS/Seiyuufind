
from email.mime import application
from fasthtml.common import fast_app,Route, Div, P, A, Hr, Titled, serve # Import all FastHTML components
import uvicorn 
app,rt = fast_app()





@app.route('/')
def home():    # The function starts here
   main_div=Div([  
P("SeiyuuFind: A reverse search engine for Voice Actors"),
Div([
P('This is a reverse search engine for voice actors. You can search for a voice actor and get a list of anime they have voiced.'),
('You can also search for an anime and get a list of voice actors who have voiced the characters in that anime.'),
('Picture and Audio will be inserted on the website..')
]),
'Made by @MMatt14 on X',

Div([
 ]),
Hr(),
 ])  # Closing parenthesis
   
   return Titled([main_div])    # Return statement is inside the function

    
styles = {
'background-color': 'black',
'color': 'white',
'text-align': 'center',
'margin': '0',
'padding': '0',
'font-family': 'Arial, Helvetica, sans-serif'
}
   
link_tag = '<link rel="stylesheet" href="C:/Users/matt1/seiyuufind/style.css">'
    
if __name__ == '__main__':

  uvicorn.run(app, host='127.0.0.1', port=8000)