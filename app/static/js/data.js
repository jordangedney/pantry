window.onload = function() {
  var source = document.getElementById('recipe-template').innerHTML;
  var template = Handlebars.compile(source);

  var data = { recipes: [
    {name: "PBJ", image: "http://lh5.ggpht.com/Cc2dlo4nRsMJcp27oHlDIWB8anQ9gTJ-nQzJC9zRu4m3Zob8oG1pS1McaU3Sfm7uGMiUaVtKMAswyq3Br4TKmv0=s230-c" },
    {name: "Pizza", image: "http://lh5.ggpht.com/Cc2dlo4nRsMJcp27oHlDIWB8anQ9gTJ-nQzJC9zRu4m3Zob8oG1pS1McaU3Sfm7uGMiUaVtKMAswyq3Br4TKmv0=s230-c" },
    {name: "Cheeseburger", image: "http://lh5.ggpht.com/Cc2dlo4nRsMJcp27oHlDIWB8anQ9gTJ-nQzJC9zRu4m3Zob8oG1pS1McaU3Sfm7uGMiUaVtKMAswyq3Br4TKmv0=s230-c" }
  ]};
  document.getElementById('content').innerHTML = template(data);
};
