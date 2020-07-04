# climatemodel
Web-based application to model, analyze, visualize, and predict global surface temperature anomalies.

This web application allows the user to analyse, visualize, and predict global surface temperature anomalies 
in degress centrigrade and per capita carbon dioxide emissions of ten countries. The web application is called
MyClimateModel and can be launched by going to the command prompt where the web application code resides on my
laptop.

* Open windows command prompt
 
* cd MyClimateModel
change directory to the location of MyClimateModel

* workon MyClimateModel 
This is a windows command which comes with virtualenvwrapper for windows. This virtualenv wrapper
lets you create many different Python environments. Working on a python project in an isolated python 
environment is recommended so that python modules and packages don’t meddle with that of other projects
or even that of the operating system.

* python routes.py. 
This starts the web application built using Flask(which is a micro web framework written in Python).

* To use the web application launch any browser either edge, chrome or firefox and access the web site by typing
http://localhost:5000

The web application has links that allows the user to do the following 

 * Temperature Anomaly Analysis
   This does the temperature anomaly analysis of global surface temperature.

 * Carbon Dioxide Emission Analysis
 
 The carbon dioxide analysis is for the countries below World, India, China, United Kingdom, United States, Nigeria
 Brazil, Australia, Japan, and Germany.
 
 
 * Carbon Offset
 
 This shows the tree offset (millions of trees) for the countries World, India, China, United Kingdom, United States, Nigeria
 Brazil, Australia, Japan, Germany.
   

REQUIREMENTS
------------

This module requires the following software modules:

 * Anaconda
 
 * Pip
 
 * VirtualEnv
 
 * VirtualEnvWrapper-win
 
 * Python Libaries: pandas, calendar, datetime, timedelta, numpy, matplotlib
 
 * Fbprophet library
 
 
 
 
 MODULES
-------------------
The modules present in the web application are the following:

* Temperature Anomaly Analysis

* Carbon Dioxide Emission Analysis

* Carbon Offset
 

INSTALLATION
------------
 
 * Install Anaconda 
 https://docs.anaconda.com/anaconda/install/windows/

  * Install VirtualEnv
  Open a command prompt and type pip install virtualenv
 
 * Install VirtualEnvWrapper-win
 Open a command prompt and type pip install virtualenvwrapper-win
 
 * Install python libraries pandas, calendar, datetime, timedelta, numpy, matplotlib
 Open a command prompt and type pip install numpy, matplotlib
 
 * Install fbprophet
 https://facebook.github.io/prophet/docs/installation.html
   

TROUBLESHOOTING
---------------

 * If all the plots and images on the Carbon Dioxide Emission Analysis page do not render click the 
  the back button on the browser. As there are visualizations for ten countries running on a development
  server the images don't render sometimes on the first instance.

MAINTAINERS
-----------

Current maintainers:
 * Yashnil Saha
