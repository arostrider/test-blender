### 1. Implement automatic testing of Blender 3.X.  
Blender 3.3 - https://www.blender.org/download/releases/3-3/  
It is necessary to develop a script that will test the operation of Blender by executing several actions.

Examples:

1. Creation of arbitrary shapes without material.
2. Creation of arbitrary shapes with material with different parameters.
3. Using different lighting with scenarios from Point 2.  


   Arguments expected as input:
   * blender_path - path to the executable file blender.exe  
   * output_path – folder where test results will be saved.  
   * x_resolution - the width of the rendered image.  
   * y_resolution - the height of the rendered image.  
   
   Expected output:  
   * Rendered image for each scenario  
   * Render log for each scenario.  
   * JSON file for each scenario, which will:  
      + Test name (optional).  
      + Date and time the test was run.  
      + The date and time the test ended.  
      + Test duration.  
      + System information (CPU, RAM, operating system name).  

   You need to independently think over the structure of the project, the implementation of tests, and also
   be ready to demonstrate and explain the solution. The results of the work must be published in a public
   repository on GitHub and sent a link.
   Useful links:
   https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html  
   https://docs.blender.org/api/current/info_quickstart.html

### 2. (optional) Implement Jenkins Pipeline Job
   
You need to implement a Jenkins Pipeline Job that will take the parameters from job 1, run the scripts
   on the connected host, and store all output files as artifacts.

   Steps to perform:

   * Install Jenkins locally  
   * Connect Jenkins node (locally)  
   * Create Job -> Pipeline  
   * Configure this project  
   * Develop a Groovy Pipeline that will do the following:  
      + Getting x_resolution and y_resolution as input parameters.  
      + Select the node you need to execute the code.  
      + Downloading a project with tests from GitHub.  
      + Running tests with x_resolution and y_resolution passed  
      + Saving test result files as run artifacts.  
   
The source code of Pipeline must be published in a public repository on GitHub and sent a link.
   Useful links:

   https://www.jenkins.io/doc/book/installing/  
   https://www.jenkins.io/doc/book/pipeline/  
   https://www.jenkins.io/doc/book/using/using-agents/