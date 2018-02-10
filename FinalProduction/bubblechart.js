
    // homelessspoptest VS TotalPop
    //relationship 2014 between homelesss population and other variables by state
        var svgWidth = 960/2;
        var svgHeight = 500/2;

        var margin = { top: 20, right: 10, bottom: 60, left: 90};

        var width = svgWidth - margin.left - margin.right;
        var height = svgHeight - margin.top - margin.bottom;

        // Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
        var svg = d3.select("#population")
        .append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        var chart = svg.append("g");

        // Append a div to the body to create tooltips, assign it a class
        d3.select("#population")
        .append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);

        d3.csv("homelesstest.csv", function(err, data) {
        if (err) throw err;

        console.log(data);
        data.forEach(function(data) {
            // x
            data.homeless = +data.homelessspoptest; 
            // y
            data.health = +data.YESHealthcoverage; 
            data.income = +data.Income; 
            // name for the bubbles
            data.state = data.Locationabbr; 
            data.population = +data.TotalPop;
        });


        // Create scale functions
        var yLinearScale = d3.scaleLinear()
            .range([height, 0]);

        var xLinearScale = d3.scaleLinear()
            .range([0, width]);

        // Create axis functions
        var bottomAxis = d3.axisBottom(xLinearScale);
        var leftAxis = d3.axisLeft(yLinearScale);

        // Scale the domain
        xLinearScale.domain([20, d3.max(data, function(data) {
            return +data.TotalPop;
        })]);
        yLinearScale.domain([0, d3.max(data, function(data) {
            return +data.homelessspoptest * 1.2;
        })]);

        var toolTip = d3.tip()
            .attr("class", "tooltip")
            .offset([80, -60])
            .html(function(data) {
            
            var stateNameFull = data.Locationdesc;
            var stateName = data.Locationabbr;
            var income = +data.Income;
            var alcohol = +data.Data_value;
            var homeless = +data.homelessspoptest; 
            var population = +data.TotalPop;

            return (stateNameFull + "<br>(" + stateName + ")<br> Income: " + income + "<br> Homelesspopulation " + homeless);
            });

        chart.call(toolTip);

        chart.selectAll("circle")
            .data(data)
            .enter().append("circle")
            .attr("cx", function(data, index) {
                // testing what is printing 
                //console.log(data.YESHealthcoverage); 
                return xLinearScale(data.TotalPop);
            })
            .attr("cy", function(data, index) {
                return yLinearScale(data.homelessspoptest);
            })
            .attr("r", function(data) {
                    return (data.Income) / 7500;
                })
            .attr("fill", "blue")
            .attr("text", "bubblename")
            .on("click", function(data) {
                toolTip.show(data);
            })
            // onmouseout event
            .on("mouseout", function(data, index) {
                toolTip.hide(data);
            });

        

        chart.append("g")
            .attr("transform", `translate(0, ${height})`)
            .call(bottomAxis);

        chart.append("g")
            .call(leftAxis);

        chart.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - margin.left )
            .attr("x", 0 - (height / 2))
            .attr("dy", "1em")
            .attr("class", "axisText")
            .text("Total Homeless Population");

        // Append x-axis labels
        chart.append("text")
            .attr("transform", "translate(" + (width / 2) + " ," + (height + margin.top + 30) + ")")
            .attr("class", "axisText")
            .text("Total US Population");
        // Append States Names to the circles (first generating the names)
        svg.selectAll("text")
        .data(data)
        .enter().append("text")
            .attr("bubblename", function(data, index) {
            console.log(data.id);
            return data.id
        });
        });
    
   