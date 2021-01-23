# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### basic.html:
{%load static%}
<!DOCTYPE HTML>
<html lang='en'>
    <head>
        <title>DK Silicon Chip PVT Ltd</title>
        <link rel="stylesheet" href="{% static 'css/website.css' %}">
        <link rel = "icon" href ="{% static 'picture/titleicon.png' %}" type = "image/x-icon">      
    </head>
    <body>
        <div class="container">
            <div class="banner">DK Silicon Chip PVT Ltd</div>
            <div class="menu">
                <div class="menuitem"><a href="/home">HOME</a></div> 
                <div class="menuitem"><a href="/products">Products</a></div> 
                <div class="menuitem"><a href="/people">People</a></div>
                <div class="menuitem"><a href="/contactus">Contact Us</a></div> 
            </div>
            <div class="content">
                {% block content %}    
                {% endblock  %}
            </div>
            <div class="footer">
                Copyright © 2020 Silicon Company Private Limited, Developed by Dineshkumar.S
            </div>
        </div>
    </body>
</html>

### home.html:
{% extends "dynamicwebsite/basic.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/picture/companybuilding.jpg" alt="Building">
    <div class="contenttext">
    DK Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
{% endblock  %}

### products.html:
{% extends "dynamicwebsite/basic.html" %}

{% block content %}
    <div class="productcontent">    
    <h1>Our Premium Products</h1>
    <div class="productitems">
        {% for i in products%}
        <div class="productitem"> 
            <div class="itemimage">
            <img src="{{i.product_img.url}}" alt="product image">
            </div>
            <div class="itemname">{{i.product_name}}</div>
            <div class="itemprice">Price:{{i.product_price}}</div>
        </div>
        {% endfor %}
    </div>
{% endblock %}

### people.html:
{% extends "dynamicwebsite/basic.html" %}

{% block content %}
    <div class="peoplecontent">
        {% for p in people %}
        <div>
            <div class="peopleimg">
                <img src= "{{ p.people_img.url }}"  alt="people image">
            </div>
            <div class="peopledetails">
                <h3>{{p.people_name}}</h3>
                <h3>{{p.people_desig}}</h3>
            </div>
        </div>
        {% endfor %}
    </div>
{% endblock %}

### contactus.html:
{% extends "dynamicwebsite/basic.html" %}

{% block content %}
    <div>
        <h2>CONTACT US</h2>
        <h3 id="h3">We're are glad to help you!</h3>
        <div>
            <form class="complaints" action="/test" method="POST">
                <textarea placeholder="Your name" rows="1" cols="50" name="name" id="name"></textarea><br>  
                <textarea placeholder="E-mail" rows="1" cols="50" name="email" id="email"></textarea><br>
                <textarea name="message" id="message" rows="8" cols="50" placeholder="Message"></textarea><br>
                <button type="submit" name="submit" id="submit">Sumbit</button>
            </form>
            <div class="contactus">
                <div>
                    <img class="address" src="https://us.123rf.com/450wm/lililia/lililia1711/lililia171100435/90687353-vector-flat-icon-of-geolocation-on-black-background.jpg?ver=6" alt="contactus">
                    <a>#140,BK nagar,Adyar,Chennai-600020</a>
                </div>
                <div>
                    <img class="address" src="https://i.pinimg.com/474x/47/ee/93/47ee9334101d8d875da877bec5f46f47.jpg" alt="contactus">
                    <a>044-2474 8291</a>
                </div>
            </div>
        </div>
    </div>
{% endblock %}


## OUTPUT:
![output](./static/picture/homepage.png)
![output](./static/picture/productspage.png)
![output](./static/picture/peoplepage.png)
![output](./static/picture/contactuspage.png)


## REPORT:
![report](./static/picture/report.png)

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://dineshkumars.student.saveetha.in . HTML code is validated.