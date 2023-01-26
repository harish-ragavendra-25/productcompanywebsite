# Web Design for a Software Product Company

## AIM:

To design a static website for a software product company company.

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

### Step 6:

Publish the website in the given URL.

## PROGRAM :
```
###home page
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <title>HR Private Limited</title>
    <link rel="stylesheet" href="static/css/layout.css" />
    <link rel="icon" href="static/img/icon.png" type="image/x-icon" />
  </head>

  <body>
    <div class="container">
      <div class="banner">HR Private Limited.</div>
      <div class="menu">
        <div class="menuitemselected"><a href="home.html">Home</a></div>
        <div class="menuitem"><a href="products.html">Products</a></div>
        <div class="menuitem"><a href="people.html">People</a></div>
        <div class="menuitem"><a href="contactus.html">Contact Us</a></div>
      </div>
      <div class="content">
        <div class="homecontent">
          <h1>About Us</h1>
          <img src="static/img/building.png" alt="Building" />
          <div class="contenttext">
            At Tally, we believe in the power of technology to make business
            owners efficient, empowered and happier, so they can focus on what
            matters most for their business. We design our products to focus on
            just that to make our products work for you, and not the other way
            around.
            <br />
            Our new product TallyPrime takes this to a new level, making your
            start to automation, or your switch to Tally simpler than ever
            before. You can now discover the product much more easily and make
            the product do more for you, without learning anything new. There is
            greater flexibility as the product adapts to your business and your
            way of working. And the transformed look and feel will only make you
            love the product even more.
            <ul>
              <li>Simple to learn, easier to use</li>
              <li>Insightful , actionable & customizable reports</li>
              <li>Anywhere, anytime and secure access</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="footer">
        Copyright &#169; 2021 HR Private Limited, Developed by HARISH RAGAVENDRA S.
      </div>
    </div>
  </body>
</html>

### products page
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <title>HR Private Limited</title>
    <link rel="stylesheet" href="static/css/layout.css" />
    <link rel="icon" href="static/img/icon.png" type="image/x-icon" />
  </head>

  <body>
    <div class="container">
      <div class="banner">HR Private Limited.</div>
      <div class="menu">
        <div class="menuitem"><a href="myapp/home.html">Home</a></div>
        <div class="menuitemselected">
          <a href="products.html">Products</a>
        </div>
        <div class="menuitem"><a href="people.html">People</a></div>
        <div class="menuitem"><a href="contactus.html">Contact Us</a></div>
      </div>
      <div class="content">
        <div class="productcontent">    
          <h1>Our Premium Products</h1>
          <div class="productitems">
              <div class="productitem"> 
                  <div class="itemimage">
                  <img src="static/img/tally_gold.png" alt="product image">
                  </div>
                  <div class="itemname">Tally Gold</div>
                  <div class="itemprice">Price: Rs.40,000.00 </div>
              </div>
              <div class="productitem"> 
                  <div class="itemimage">
                  <img src="static/img/tally_silver.png"  alt="product image">
                  </div>
                  <div class="itemname">Tally Silver</div>
                  <div class="itemprice">Price: Rs.10,000.00 </div>
              </div>
          </div>
          </div>        
      </div>
      <div class="footer">
        Copyright &#169; 2021 HR Private Limited, Developed by Obed Otto.
      </div>
    </div>
  </body>
</html>

### peoples page
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <title>HR Private Limited</title>
    <link rel="stylesheet" href="static/css/layout.css" />
    <link rel="icon" href="static/img/icon.png" type="image/x-icon" />
  </head>

  <body>
    <div class="container">
      <div class="banner">HR Private Limited.</div>
      <div class="menu">
        <div class="menuitemselected"><a>Home</a></div>
        <div class="menuitem"><a href="products.html">Products</a></div>
        <div class="menuitem"><a href="people.html">People</a></div>
        <div class="menuitem"><a href="contactus.html">Contact Us</a></div>
      </div>
     <div>>
         <img src="static/img/elon.jpeg">
         <h1>ELON MUSK<h2>
     </div>
    <div>
        <img src="static/sundar.jpeg">
        <h1>SUNDAR PICHAI</h1>
    </div>
    <div>
        <img src="Tony_Stark.jpg">
        <h1>TONY STARKs</h1>
    </div>
    <div class="footer">
        Copyright &#169; 2021 HR Private Limited, Developed by HARISH RAGAVENDRA S.
      </div>
    </div>
  </body>
</html>

###contactus page
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <title>HR Private Limited</title>
    <link rel="stylesheet" href="static/css/layout.css" />
    <link rel="icon" href="static/img/icon.png" type="image/x-icon" />
  </head>

  <body>
    <div class="container">
      <div class="banner">HR Private Limited.</div>
      <div class="menu">
        <div class="menuitemselected"><a href="home.html">Home</a></div>
        <div class="menuitem"><a href="products.html">Products</a></div>
        <div class="menuitem"><a href="people.html">People</a></div>
        <div class="menuitem"><a href="contactus.html">Contact Us</a></div>
      </div>
      <div>
          <p>
            contactus: hroffice@gmail.com<br>
            phoneno: 7339174377
          </p>
      </div>
     
      <div class="footer">
        Copyright &#169; 2021 HR Private Limited, Developed by HARISH RAGAVENDRA S.
      </div>
    </div>
  </body>
</html>


```
## OUTPUT:
![output](./images/product.png)
![output](./images/contactus.png)
![output](images/people.png)
![output](home1.png)


### Home Page:

![output](./images/homepage.jpg)
## Result:

Thus a website is designed for the software product company and the HTML,CSS code are validated.
