# CyberBullying-Detection-in-Hinglish-Languages-Using-Machine-Learning-

<img src="Output/front_photo.jpeg" width="520" >

## Table of Content

 1. Overview
 2. Learning-Objective
 3. Technologies-used
 4. Technical-aspect
 5. Design and Artitecture 
 7. installation
 8. Steps to write python flask app
 9. Output 


### Overview :- 

we created a bot around the whatsapp platform which interact with users and used twilio which is used to utilize the the service because it offers an API in whatsapp and whenever we create bot we always need to send the response back for the given message and for that we used python language and flask framework.

### Learning Objective :- 

The following points were the objective of the project . If you are looking for all the following points in this repo then i have not covered all in this repo. I'm working on blog about this mini project and I'll update the link of blog about all the points in details later . (The main intention was to create an end-to-end chatbot application. )  
- Setting up whatsapp chastbot.
- Integrate with twillio API.
- Setting up Webhooks securely using flask.
- Wrtitng python handlers.
- Fetching stock data with Marketstack.

### Technologies Used :- 

![](https://forthebadge.com/images/badges/made-with-python.svg) 

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=100>
<img target="_blank" src="https://backendless.com/wp-content/uploads/2020/04/twilio-logo.png" width=70>
<img target="_blank" src="https://www.freepnglogos.com/uploads/whatsapp-png-image-9.png" width=65>
<img target="_blank" src="https://symbols.getvecta.com/stencil_27/122_webhooks.82c05a6373.svg" width=65>
<img target="_blank" src="https://cms-assets.tutsplus.com/uploads/users/769/posts/35539/preview_image/marketstack.jpg" width=75>]

### Technical Aspect :- 

<img src="Output/Tech_component.png" width="550" >

- created a bot around the whatsapp platform which interact with users
- used twilio which is used to utilize the the service because it offers an API in whatsapp.
- Twilio can only send data over https for the security stacke.
- so to overcome this we used Ngrok, it help us to create an HTTP turnel, it basically turnels the https traffic to our local host.
- whenever we create bot we always need to send the response back for the given message and for that we used python language and flask framework.
- flask app created now will help use to talk to markert stack API.
  
#### Why whatsapp Bot ?

- 2 Billion users base. 
- Most popular messaging app. 
- end to end encrytion of security. 
- easy to integrate for developers. 
- backed by facebook for buisness users.

#### what are webhooks ?

- HTTPS and API endpoints, which recieves data in json format or any format which is supported by HTTPS. 
- Recieve HTTP request over TLS/SSL. 
- call the revelant handlers. 
- performed Buisness Logic.
- Returns the response.

#### why python flask for webhooks ?

- few lines require to write webapp. 
- Easy to understand.
- Quick to setup and get going. 
- very light weight 
- can be easily extended with more packages as app evolves.

#### why market stacks ?
 
- easy to get started. 
- includes 72 stock exchanges.
- Light weight json API. 
- Extensive documentation. 
- Easy support for python.


### Design and Architecture :- 

<img src="Output/Artitecture.png" width="850" >

#### 1. Whatsapp - Twilio
- User sends message to twilio provided sandbox url & twilio recieves the message. 

#### 2. Twilio - python flask App 
- calls thew registered webhooks and sends data & flaskapp recives the Requerst.

#### 3. python flask app - Marketstack 
- parse data and gets stock data from Marketstack & marketstack API returns the stack price data. 


### Installation :- 

- Clone this repository and unzip it.
- After downloading, cd into the flask directory.
- Begin a new virtual environment with Python 3 and activate it.
- Install the required packages using pip install -r requirements.txt
- Execute the command: python app.py.


### Steps to write python flask app :- 

- Installed python 
- created the virtual environment 
- created a requirement.txt files for dependencies. 
- Installed flask 
- Installed requests (useful when we integrate market stack)
- installed twilio (for interacting with twilio)

### Output

<img src="Output/out_1.jpg" width="320" >

<img src="Output/out_2.jpg" width="320" >

<img src="Output/out_3.jpg" width="320" >


###  Made with &nbsp;❤️ by  [Karan Shah](https://karanshah1910.tech/) 





