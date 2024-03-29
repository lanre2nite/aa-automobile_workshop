<!--
   ALX SE PROGRAM
   PORTFOLIO PROJECT
   COHORT 12
   AA Autombile Workshop
   index.html
   
   Copyright 2024  <aaie@raspberrypi>

-->

<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAseFWMq_L_0MLee8GLB3y2KcPJLTuifDs&libraries=places,directions"></script>
<title>Homepage - AA-Automobile Workshop</title>
        <link rel="stylesheet"
    type="text/css"
    href= "aaaw-style.css">
</head>
<body>
    <!-- Header -->
  <header class="header" data-section-theme="dark">
      <div class="container">
        <div class="header-logo">
          <a href="#">
    <img src="logo.jpg" alt="Techium logo" width="100" height="20">
          </a>
        </div>
        <nav class="navbar-menu">
          <ul class="nav">
            <li class="nav-item">
              <a href="#" class="nav-link">Home</a>
            </li>
            <li class="nav-item">
              <a href="#services" class="nav-link">Services</a>
            </li>
                        <li class="nav-item">
              <a href="#login" class="nav-link">Login</a>
            </li>
            <li class="nav-item">
              <a href="#blog" class="nav-link">Blog</a>
            </li>
                        <li class="nav-item">
              <a href="#about" class="nav-link">About Us</a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
    <!-- Main -->
    <main>
      <h1 class="visually-hidden">AA Automobile Workshop</h1>
      
      <!-- Hero section -->
      <!--section class="section-hero" data-section-theme="dark"-->
        <div class="container">
          <div class="section-body">
            <section class="section-inner">
                <h2 class="section-title">AA Automobile Workshop</h2>
                        <h4>Automobile Diagnosis, Repair and Maintenance Made Easy and Available</h4>
                        <h4>Anywhere and Everywhere!</h4> 
                        <img src="image1.jpg" alt="Techium logo" width="1200" height="300">
                    </section>
          </div>
        </div>
        
      </section>
      <!-- Services section -->
      <section id="services" class="section">
        <div class="container">
          <header class="section-header">
            <h2 class="section-title">Services</h2>
            <p class="section-tagline">Comfort and Mobility Always!</p>
          </header>
          <div class="section-body">
            <ul class="row">
              <li class="col-1-3">
                <div class="card-services">
                  <h3 class="card-title"><a href="#">Automobile System Diagnosis</a></h3>
                </div>
              </li>
              <li class="col-1-3">
                <div class="card-services">
                  <h3 class="card-title"><a href="#">Automobile Systems/Devices Maintenance</a></h3>
                </div>
              </li>
              <li class="col-1-3">
                <div class="card-services">
                  <h3 class="card-title"><a href="#">Automobile Systems Design & Installations</a></h3>
                </div>
              </li>
            </ul>
            <ul class="row">
              <li class="col-1-3">
                <div class="card-services">
                  <h3 class="card-title"><a href="#">Auto Parts Replacement</a></h3>
                </div>
              </li>
              <li class="col-1-3">
                <div class="card-services">
                  <h3 class="card-title"><a href="#">Sales & Consultancy Services</a></h3>
                </div>
              </li>
              <li class="col-1-3">
                <div class="card-services">
                  <h3 class="card-title"><a href="#">Schedule Repair with a Mechanic near U</a></h3>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </section>
<!-- Login -->
<section id= "login" class="section">
  <div class="container">
    <header class="section-header">
      <h2 class="''section-ttitle">Login</h2>
    </header>
<h5>Kindly login with your email and password e.g gmail/hotmail/yahoomail</h5>
<form action="/login" method="post">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" required><br><br>
  <label for="password">Password:</label>
  <input type="password" id="password" name="password" required>
  <button type="submit">Login</button><br><br>
</form>
   <div id="map"></div>
  <div id="search-box"></div>
  <div id="directions-panel"></div>
  <button id="traffic-toggle">Traffic of my Location</button>
  <script>
    // Replace YOUR_API_KEY with your actual API key
    const YOUR_API_KEY = "AIzaSyAseFWMq_L_0MLee8GLB3y2KcPJLTuifDs";

    function initMap() {
      const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: { lat: 9.0579, lng: 7.4951 }
      });

      // Create search box
      const searchBox = new google.maps.places.SearchBox(document.getElementById("search-box"));
      searchBox.addListener("places_changed", () => {
        const places = searchBox.getPlaces();
        if (places.length > 0) {
          const place = places[0];
          map.setCenter(place.geometry.location);
          new google.maps.Marker({
            position: place.geometry.location,
            map: map
          });
        }
      });

      // Directions panel
      const directionsPanel = document.getElementById("directions-panel");

      // Directions service and renderer
      const directionsService = new google.maps.DirectionsService();
      const directionsRenderer = new google.maps.DirectionsRenderer({
        map: map,
        panel: directionsPanel
      });

      // Traffic layer
      const trafficLayer = new google.maps.TrafficLayer();

      // Toggle traffic button
      const trafficButton = document.getElementById("traffic-toggle");
      trafficButton.addEventListener("click", () => {
        trafficLayer.setMap(trafficLayer.getMap() ? null : map);
      });

      // Example direction calculation
      const origin = { lat: 9.0579, lng: 7.4951 };
      const destination = { lat: 9.0579, lng: 7.4951 };

      directionsService.route({
        origin: origin,
        destination: destination,
        travelMode: google.maps.TravelMode.DRIVING
      }, (response, status) => {
        if (status === google.maps.DirectionsStatus.OK) {
          directionsRenderer.setDirections(response);
        }
      });
    }

    window.addEventListener("load", initMap);
  </script> 
  </div>
   <!-- Blog section -->
      <section id="blog" class="section">
        <div class="container">
          <header class="section-header">
            <h2 class="section-title">Blog</h2>
            <p class="section-tagline">Follow Us for Exciting Updates about the Automobile Industry</p>
          </header>
          <div class="section-body">
            <div class="row">
              <div class="col-1-2">
                <img src="diagnostic2.jpg" alt="" width="460" height="460">
              </div>
              <div class="col-1-2">
                <P> Welcome!, this my first blog, Title: Best Electric Vehicle 2024</P>
                <p>The Hyundai Ioniq 5 takes our Best Electric Vehicle award for the second year in a row because it continues to hit a near-ideal balance of attributes — even against newer competitors. It offers a roomy, versatile cabin within relatively tidy exterior dimensions; avant-garde styling that doesn’t neglect everyday practicality; and a simple, easy-to-use control layout that still packs in lots of useful technology features.</p>
                <p>The Ioniq 5 debuted for 2022, and for 2024, it comes standard with rear side impact airbags (in addition to the previously standard side curtain airbags), a Wi-Fi hot spot and steering-wheel haptic feedback for the blind spot collision avoidance and lane departure steering assist systems. On the top Limited trim, a digital rearview-mirror camera display is newly standard. If the all-wheel-drive Ioniq 5’s 320 horsepower isn’t spicy enough for you, sit tight: A high-performance Ioniq 5 N variant with up to 641 hp is slated to arrive for 2024.</p>
                <p>The average driver should find the Ioniq 5 plenty quick, however: An AWD Limited model did 0-60 mph in an impressive 4.72 seconds in our testing. Charging via a 350-kilowatt DC fast charger is quick, too, thanks to the Ioniq’s 800-volt architecture that has proven to be a real-world advantage when we’ve tested the Ioniq 5’s fast charging alongside competitors. For home charging, there’s a standard 10.9-kW onboard charger, and there’s also what Hyundai calls vehicle-to-load capability on Limited trims that lets you use the Ioniq 5’s high-voltage battery as a mobile power source via two AC household outlets, one in an available adapter in the charge port and the second in an outlet under the backseat. The Ioniq 5’s range is respectable, as well: AWD models are EPA-rated up to 260 miles on a full charge, the rear-wheel-drive version up to 303 miles.</p>
                <p>Source: https://www.cars.com/articles/best-electric-vehicle-of-2024-476755/</p>
              </div>
            </div>
          </div>
    <!-- About Us-->
    <section id="about" class="section">
      <div class="container">
        <header class="section-header">
            <h2 class="section-title">About US</h2>
            <p class="section-tagline">At Your Service Always</p>
          </header>
        <h3>Who are we</h3>
                <p>AA Integrated Limited is a Nigerian Indigenous Company established in mid 2020s and registered with the Corporate Affairs on the 13th October 22020 to provide optimized solutions for individuals, public and private sector while catering for all there engineering needs. 
                We specialize in Computer, Mechanical & Electrical/Electronic Systems Installations, Sales of Accessories/ Devices/Equipment, Maintenance & Repairs.
Engineering is a profession concerned primarily with the application of a certain body of knowledge, set of skills and point of view in the creation of devices, systems, processes and structures used to transform resources to forms which satisfy the needs of the society.
We are team of versatile engineers with many years of technical and administrative experience and we take pride in satisfying our client’s needs by providing the optimal services using the best materials and devices.
</p>
                
                <h4>VISION</h4>
<p>OUR Vision is to be pinnacle of the Nigerian engineering firm that would be capable of providing the best efficient services and be an exemplary model to other engineering firms.</p>
<h4>MISSION</h4>
<p>OUR Mission is to give our clients the opportunity to acquire the optimal services to enhance their daily life and business wellness from well trained, experience and professional experts.</p>
                <h3>How we work</h3>
                <p>We promote client's services and also collaborate with them to actualize there digital presence</p>
        <h5>The company’s registered office address is No 32 Near Fifteen (15) Shop Shopping Complex, Along Federal High Court, Polo, Maiduguri, Borno state, Nigeria.
          <h5>Operating Address is FHA Lugbe, FCT Abuja</h5>
<h5>Contact Phone: +2348120207258</h5> 
<a href="mailto: aaintegrated@outlook.com">Email: aaintegrated@outlook.com</a><br>
<a href>Website: aaintegrated.business.site</a>
<form action="your_script.php" method="post">
  <h4>Feedback Form</h4>
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" placeholder="Your Name">
  <br><br>
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" placeholder="Your Email">
  <br><br>
  <label for="message">Message:</label>
  <textarea id="message" name="message" cols="30" rows="10" placeholder="Write your message here"></textarea>
  <br>
  <button type="submit">Send Message</button>
</form>
      </div>
    </section>
</body>
<!-- Footer -->

    <!--<footer class="footer" data-section-theme="dark"-->
      <div  class="container">
<h5 style="text-align: center;">AA INTEGRATED LIMITED RC 1721493 | Copyright &copy; 2024</h5>
      </div>
    </footer>
</html>

###This is a README.md file
### ALX SE PROGRAM
#TOPIC: PROJECT PORTFOLIO
##AA AUTOMOBILE WORKSHOP
