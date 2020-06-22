var tree;
var blocks;
var tracking=0;
var username;

//Tree Context Menu Structure
var contex_menu = {
    'context1' : {
        elements : [
            {
                text : 'Node Actions',
                icon: 'static/webapp/animara/images/blue_key.png',
                action : function(node) {

                },
                submenu: {
                    elements : [
                        {
                            text : 'Toggle Node',
                            icon: 'static/webapp/animara/images/leaf.png',
                            action : function(node) {
                                node.toggleNode();
                            }
                        },
                        {
                            text : 'Expand Node',
                            icon: 'static/webapp/animara/images/leaf.png',
                            action : function(node) {
                                node.expandNode();
                            }
                        },
                        {
                            text : 'Collapse Node',
                            icon: 'static/webapp/animara/images/leaf.png',
                            action : function(node) {
                                node.collapseNode();
                            }
                        },
                        {
                            text : 'Expand Subtree',
                            icon: 'static/webapp/animara/images/tree.png',
                            action : function(node) {
                                node.expandSubtree();
                            }
                        },
                        {
                            text : 'Collapse Subtree',
                            icon: 'static/webapp/animara/images/tree.png',
                            action : function(node) {
                                node.collapseSubtree();
                            }
                        },
                    ]
                }
            },
            {
                text : 'Remove Module',
                icon: 'static/webapp/animara/images/delete.png',
                action : function(node) {
                    node.removeModule();
                }
            }
        ]
    }
};



(function(){





    blocks = new Blocks();

    blocks.types.addCompatibility('string', 'number');
    blocks.types.addCompatibility('string', 'bool');
    blocks.types.addCompatibility('bool', 'number');
    blocks.types.addCompatibility('bool', 'integer');
    blocks.types.addCompatibility('bool', 'string');

    blocks.run('#blocks');
    blocks.load({"blocks":[],"edges":[]});

    function saveToFile(text) {
        var pom = document.createElement('a');
        pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        pom.setAttribute('download', "export.json");

        if (document.createEvent) {
            var event = document.createEvent('MouseEvents');
            event.initEvent('click', true, true);
            pom.dispatchEvent(event);
        }
        else {
            pom.click();
        }
    }

    blocks.ready(function() {
        blocks.menu.addAction('Export', function(blocks) {
            saveToFile(JSON.stringify(blocks.export(),null,4));
        }, 'export');

        $('.setLabel').click(function() {
            for (k in blocks.edges) {
                var edge = blocks.edges[k];
                edge.setLabel('Edge #'+edge.id);
            }
        });

        $('.setInfos').click(function() {
            for (k in blocks.blocks) {
                var block = blocks.blocks[k];
                block.setInfos('Hello, I am the block #'+block.id);
            }
        });

        $('.setDescriptions').click(function() {
            for (k in blocks.blocks) {
                var block = blocks.blocks[k];
                block.setDescription('This is the block #'+block.id);
            }
        });

        $('.resize').click(function() {
            $('#blocks').width('300px');
            blocks.perfectScale();
        });

        $('.hideIcons').click(function() {
            blocks.showIcons = false;
            blocks.redraw();
        });

        $('#undo').click(function() {
            blocks.history.restoreLast();
        });


        $('.loadBlocks').click(function() {

            var file=document.createElement("input");
            file.setAttribute("type","file");
            $(file).change(
                function (e) {
                    var fr = new FileReader();
                    fr.onload=function(e){
                        blocks.register(JSON.parse(e.target.result));
                    }
                    fr.readAsText(e. target. files[0]);
                }
            );

            if (document.createEvent) {
                var event = document.createEvent('MouseEvents');
                event.initEvent('click', true, true);
                file.dispatchEvent(event);
            }
            else {
                file.click();
            }
        });
        $('#open').click(function() {

            var file=document.createElement("input");
            file.setAttribute("type","file");
            $(file).change(
                function (e) {
                    var fr = new FileReader();
                    fr.onload=function(e){
                        blocks.clear();
                        blocks.load(JSON.parse(e.target.result));
                    }
                    fr.readAsText(e. target. files[0]);
                }
            );

            if (document.createEvent) {
                var event = document.createEvent('MouseEvents');
                event.initEvent('click', true, true);
                file.dispatchEvent(event);
            }
            else {
                file.click();
            }
        });

        $('#save').click(function () {
            saveToFile(JSON.stringify(blocks.export(),null,4));
        });

        $('#clear').click(function () {
            alertify.confirm('Workflow Designer','Clear Workflow?', function(){ clearTracking(); blocks.clear(); }, function(){});
        });

        $("#importSubmit").click(function (event) {

            event.preventDefault();
            // Get form

            // Create an FormData object
            var formData = new FormData(document.getElementById('fileUploadForm'));

            alertify.notify("Please Wait", 'success', 2);

            $.ajax({
                type: "POST",
                enctype: 'multipart/form-data',
                url: "api/workflow/upload",
                data: formData,
                processData: false, 
                contentType: false,
                cache: false,
                timeout: 600000,
                beforeSend: function(request) {
                    request.setRequestHeader("email",  $.cookie("email"));
                    request.setRequestHeader("token",  $.cookie("token"));
                },
                success: function (data) {
                    // console.log(data)
                    // var num_of_new_blocks = JSON.parse(data);
                    // blocks.register(newBlocks);
                    initializeTree();
                    // if(newBlocks.length!=0)
                    if(data.new_block_length!=0)
                        alertify.notify(data.new_blocks_length + ' blocks registered', 'success', 5);
                    else{
                        alertify.notify('No blocks registered', 'error', 5);
                    }
                    // console.log("--------------------------------------------formdata");
                    // console.log(data);
                    // console.log("--------------------------------------------formdata");
                },
                error: function (e) {
                    alertify.notify('Error Registering blocks', 'error', 3);
                    if(e.status===403){
                        alertify.notify(e.responseText, 'error', 15);
                    }
                    if(e.status===400){
                        alert("Error!"+e.responseText);
                    }
                }
            });

        });

        /*
        $("#execute").click(function(event){
            clearTracking();
            alertify.notify('Workflow Execution Started', 'success', 5);

            for (k in blocks.blocks) {
                var block = blocks.blocks[k];
                block.setInfos('');
                $(block.div[0]).removeClass("block_completed");
                $(block.div[0]).removeClass("block_error");
            }

            document.getElementById("modals").innerHTML="";

            // Create an FormData object
            var data = new FormData();

            // If you want to add an extra field for the FormData
            data.append("workflow", JSON.stringify(blocks.export()));

            $.ajax({
                type: "POST",
                enctype: 'multipart/form-data',
                url: "api/workflow/execute",
                data: data,
                processData: false,
                contentType: false,
                cache: false,
                timeout: 600000,
                success: function (data) {
                    data = JSON.parse(data);
                    populateOutputs(data);
                    alertify.notify('Workflow Execution Completed!', 'success', 3);
                },
                error: function (e) {
                    alertify.notify(e.responseText, 'error', 3);
                }
            });
        });
        */

        $("#schedule").click(function(event){

            for (k in blocks.blocks) {
                var block = blocks.blocks[k];
                block.setInfos('');
            }

            document.getElementById("modals").innerHTML="";

            // Create an FormData object
            var data = new FormData();

            // If you want to add an extra field for the FormData
            data.append("workflow", JSON.stringify(blocks.export()));
            data.append("email", $.cookie("email"));

            $.ajax({
                type: "POST",
                enctype: 'multipart/form-data',
                url: "api/workflow/schedule",
                data: data,
                processData: false,
                contentType: false,
                cache: false,
                timeout: 600000,
                beforeSend: function(request) {
                    request.setRequestHeader("email",  $.cookie("email"));
                    request.setRequestHeader("token",  $.cookie("token"));
                },
                success: function (data) {
                    tracking=data.job_id;
                    alertify.notify('Job ID '+data.job_id+' scheduled !', 'success', 3);
                    track(tracking);
                },
                error: function (e) {
                    alertify.notify(e.responseText, 'error', 3);
                    if(e.status===400){
                        alert("Error!"+e.responseText);
                    }
                }
            });
        });

    });

    $(document).ready(function () {

        $(".toggle-sidebar").click(function(){
            $("#sidebar").toggleClass("collapsed");
            $("#content").toggleClass("col-md-12 col-md-9");
        });
        var jobUpdater;
        $('#jobsModal').on('shown.bs.modal', function (e) {
            updateJobsTable();
            jobUpdater=setInterval(function(){
                try{
                    updateJobsTable();
                }
                catch(e){
                    //Unauthorized
                }

            },3000);
        })
        $('#jobsModal').on('hide.bs.modal', function (e) {
            clearInterval(jobUpdater)
        });



        if($.cookie("email")){
            $("#myAccount").show();
            $("#login").hide();
            $("#mainMenu").show();
            $("#schedule").show();
            document.getElementById("myAccountButton").innerHTML="Hi, "+$.cookie("email");
        }
        else{
            $("#myAccount").hide();
            $("#login").show();
            $("#mainMenu").hide();
            $("#schedule").hide();
        }


        //Creating the tree

        if(!$.cookie("email")){
            $('#loginModal').modal('show');
        }
        else {
            $('#elfinder').elfinder({
                url : 'elfinder/connector'
            });
            initializeTree();
        }

    });



})();


function initializeTree() {
    tree = createTree('div_tree','white',contex_menu);

    //Rendering the tree
    tree.drawTree();

    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "api/workflow/initialize",
        processData: false,
        contentType: false,
        cache: false,
        beforeSend: function(request) {
            request.setRequestHeader("email",  $.cookie("email"));
            request.setRequestHeader("token",  $.cookie("token"));
        },
        timeout: 600000,
        success: function (data) {
            // var blockDefinitions = JSON.parse(data)
            var blockDefinitions = data
            blocks.register(blockDefinitions);

            var library=[];
            var permissions=[];
            for(i=0;i<blockDefinitions.length;i++){

                var jar = blockDefinitions[i].module.split(":")[0];
                var package = blockDefinitions[i].module.split(":")[1];
                var family = blockDefinitions[i].family;
                var name = blockDefinitions[i].name;
                var public = (blockDefinitions[i].public==true);

                if(!library[jar]){
                    library[jar]=[];
                }
                if(!library[jar][package]){
                    library[jar][package]=[];
                }
                if(!library[jar][package][family]){
                    library[jar][package][family]=[];
                }
                library[jar][package][family].push(name);
                permissions[jar]=public;

            }

            //Loop to create test nodes
            for (var jar in library) {
                var node1;
                if(permissions[jar]!==true)
                    node1 = tree.createNode(jar,false,'static/webapp/animara/images/key.png',null,null,'context1');
                else
                    node1 = tree.createNode(jar,false,'static/webapp/animara/images/group.png',null,null,'context1');
                for(var package in library[jar]){
                    var node2 = node1.createChildNode(package,false,'static/webapp/animara/images/leaf.png',null,null,'context1');
                    for(var family in library[jar][package]){
                        var node3 = node2.createChildNode(family, false, 'static/webapp/animara/images/blue_key.png',null,'context1');
                        for(var i=0;i<library[jar][package][family].length; i++){
                            node3.createChildNode(library[jar][package][family][i], false, 'static/webapp/animara/images/monitor.png',null,'context1');
                        }
                    }
                }


            }
            // console.log("--------------------------------------------===========");
            // console.log(data);
        },
        error: function (e) {
            alert("Error!"+e.responseText);
        }
    });

}

function expand_all() {
    tree.expandTree();
}


function collapse_all() {
    tree.collapseTree();
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev,node_id) {
    // console.log("--------------------------------------------");
                    // console.log(data);
    var rel = getBlockRel(tree,node_id);
    var module = getBlockModule(tree,node_id);
    for(var meta in blocks.metas){
        if(blocks.metas[meta].name===rel){
            ev.dataTransfer.setData("rel", rel);
            ev.dataTransfer.setData("module",module);
            return;
        }
    }
    ev.preventDefault();
}

function drop(ev) {
    var rel = ev.dataTransfer.getData("rel");
    var module = ev.dataTransfer.getData("module");
    var blocksPosition = $("#blocks").offset();
    blocks.addBlock(rel, module, ev.clientX-blocksPosition.left-blocks.center.x, ev.clientY-blocksPosition.top-blocks.center.y);
}

function getBlockRel(tree,node_id){
    var node=tree;
    for(var child in node.childNodes){
        if(node.childNodes[child].id==node_id){
            return node.childNodes[child].text;
        }
        else{
            var inChildren = getBlockRel(node.childNodes[child],node_id);
            if(inChildren)return inChildren;
        }
    }
}

function getBlockModule(tree,node_id){
    var node=tree;
    for(var child in node.childNodes){
        if(node.childNodes[child].id==node_id){
            return node.parent.parent.text+":"+node.parent.text;
        }
        else{
            var inChildren = getBlockModule(node.childNodes[child],node_id);
            if(inChildren)return inChildren;
        }
    }
}

function updateJobsTable(){

    $.ajax({
        type: "GET",
        url: "api/workflow/schedule",
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        beforeSend: function(request) {
            request.setRequestHeader("email",  $.cookie("email"));
            request.setRequestHeader("token",  $.cookie("token"));
        },
        success: function (data) {
            data=JSON.parse(data);
            var table=$("#jobTable");
            $("#jobTable tbody").empty();
            for(var i=0;i<data.length;i++){
                var job=data[i];
                var row="<tr><td>"+job.id+"</td><td>"+job.startTime+"</td><td>"+job.endTime+"</td><td>"+job.status+"</td><td><button onclick='getWorkflow("+job.id+")' class='btn btn-default'>Load</button></td></tr>"
                table.append(row);
            }
        },
        error: function (e) {
            if(e.status===400){
                alert("Error!"+e.responseText);
            }
        }
    });
}

function track(jobId){
    tracking=jobId;
    var intervalID=setInterval(function(){getWorkflowStatus(tracking,intervalID)},1000);
}

function clearTracking() {
    var jobStatus= document.getElementById("jobStatus");
    jobStatus.innerHTML="";
    tracking=0;
}

function getWorkflow(jobId){
    var formData = new FormData();
    formData.append("jobId", jobId);
    if(jobId===0) return;
    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "api/workflow/jobs",
        data: formData,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        beforeSend: function(request) {
            request.setRequestHeader("email",  $.cookie("email"));
            request.setRequestHeader("token",  $.cookie("token"));
        },
        success: function (data) {
            data=JSON.parse(data);
            blocks.clear();
            blocks.load(data.workflow);
            console.log("==================================");
            console.log(data.workflow);
            console.log("==================================");
            var jobStatus= document.getElementById("jobStatus");
            jobStatus.innerHTML="Job ID:"+data.id+" Status:"+data.status+" Start Time:"+data.startTime+
                " End Time:"+data.endTime;
            if(data.status!=="COMPLETED"||data.status!=="FAILED"){
                track(jobId);
            }
            $('#jobsModal').modal('toggle');
        },
        error: function (e) {
            if(e.status===400){
                alert("Error!"+e.responseText);
            }
        }
    });
}

function clearSchedule(jobId){
    if(jobId===0) return;
    $.ajax({
        type: "DELETE",
        url: "api/workflow/schedule",
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        beforeSend: function(request) {
            request.setRequestHeader("email",  $.cookie("email"));
            request.setRequestHeader("token",  $.cookie("token"));
        },
        success: function () {
            updateJobsTable();
        },
        error: function (e) {
            if(e.status===400){
                alert("Error!"+e.responseText);
            }
        }
    });
}

function getWorkflowStatus(jobId,intervalId){
    if(jobId==0){
        clearInterval(intervalId);
        return;
    }
    var data = new FormData();
    data.append("jobId", jobId);
    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "api/workflow/jobs",
        data: data,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        beforeSend: function(request) {
            request.setRequestHeader("email",  $.cookie("email"));
            request.setRequestHeader("token",  $.cookie("token"));
        },
        success: function (data) {
            data=JSON.parse(data);
            var jobStatus= document.getElementById("jobStatus");
            jobStatus.innerHTML="Job ID:"+data.id+" Status:"+data.status+" Start Time:"+data.startTime+
                " End Time:"+data.endTime;
            if(data.executionStatus)
                populateOutputs(data.executionStatus);
            else
                populateOutputs(data.workflow.blocks);
            if(data.status==="COMPLETED"||data.status==="FAILED"){
                clearInterval(intervalId);
                tracking=0;
            }
        },
        error: function (e) {
            if(e.status===400){
                alert("Error!"+e.responseText);
            }
        }
    });
}

function populateOutputs(data){
    for (var k in blocks.blocks) {
        var block = blocks.blocks[k];

        for(var x in data){
            if(data[x].id===block.id){

                if(data[x].completed)block.div[0].setAttribute("class","block block_completed");
                else {
                    $(block.div[0]).removeClass("block_completed");
                    $(block.div[0]).removeClass("block_error");
                }
                if(data[x].output||data[x].stderr||data[x].stdout){
                    var output = 'Output:';
                    if(data[x].output){

                        var outputObj = data[x].output;
                        if (outputObj.type==="STRING"){
                            output+=outputObj.value;
                        }
                        else if (outputObj.type==="FILE"){
                            output+="<a href=\"api/workflow/file/"+outputObj.value.filename+"\">"+outputObj.value.title+"</a>";
                        }
                        else if (outputObj.type==="TABLE"){
                            output+="<br/>"+
                                '<a href="api/workflow/file/'+outputObj.value.filename+'"><button class="btn btn-success btn-sm" >Download Table</button></a>'+
                                '<a href="csv.html?csv='+outputObj.value.filename+'" target="_blank"><button class="btn btn-success btn-sm" >Open</button></a>';

                        }
                        else if (outputObj.type==="GRAPH"){
                            output+="<br/>"+
                                '<a href="api/workflow/file/'+outputObj.value.filename+'"><button class="btn btn-success btn-sm" >Download Graph Data</button></a>'+
                                '<a href="graph.html?graph='+outputObj.value.filename+'" target="_blank"><button class="btn btn-success btn-sm" >Open</button></a>';
                        }
                    }

                    var showDebug = $( "#logLevel" ).prop("checked");

                    if((data[x].stdout && showDebug) || data[x].stderr){
                        if(data[x].error)block.div[0].setAttribute("class","block block_error");
                        var modal = document.getElementById("logModal");
                        var div = document.createElement('span');
                        div.innerHTML=modal.innerHTML;

                        if(data[x].stdout) div.getElementsByClassName("stdout")[0].innerHTML="<h5 class=\"modal-title\">Output Stream:</h5>"+data[x].stdout.replace(new RegExp('\r?\n','g'), '<br />');
                        div.getElementsByClassName("stderr")[0].innerHTML="<h5 class=\"modal-title\">Error Stream:</h5>"+data[x].stderr.replace(new RegExp('\r?\n','g'), '<br />');
                        div.getElementsByClassName("modal fade")[0].setAttribute("id", "logModal"+block.id);
                        document.getElementById("modals").innerHTML+=div.innerHTML;
                        output+="<br/>"+
                            '<button class="btn btn-primary btn-sm" href="#"  data-toggle="modal" data-target="#logModal'+block.id+'">Show Log</button>';
                    }

                    block.setInfos(output);
                }

            }
        }

    }

}
function selectFile(event,target){
    event.preventDefault();
    button=target;

    $('#browseModal').on('shown.bs.modal', function (e) {
        $('#browseModal').css('z-index',9999);
        $('#elfinderBrowse').elfinder({
            url : 'elfinder/connector',
            commandsOptions:{
                getfile: {
                    oncomplete: 'destroy'
                }
            },
            getFileCallback : function(file)
            {
                $('#browseModal').modal('hide');
                button.innerHTML=file.path;
                button.nextSibling.value=file.path;
            }
        });
    });
    $('#elfinderBrowse').on('hide.bs.modal', function (e) {
        if($('#elfinderBrowse').html()!="")
            $('#elfinderBrowse').elfinder('destroy');
    });
    $('#browseModal').modal('show');

}

function logout(){
    $.removeCookie("email");
    $.removeCookie("name");
    clearTracking();
    //Clearing blocks
    blocks.clear();
    //Clearing Tree
    tree = createTree('div_tree','white',contex_menu);
    tree.drawTree();

    //Clearing elfinder
    try{
        if($('#elfinder').html()!="")
            $('#elfinder').elfinder("destroy");
    }
    catch(e){
       //Already destroyed
    }
    try{
        if($('#elfinderBrowse').html()!="")
        $('#elfinderBrowse').elfinder("destroy");
    }
    catch(e){
        //Already destroyed
    }

    $('#myAccount').hide();
    $('#login').show();
    $('#mainMenu').hide();
    $('#schedule').hide();
}

function showRegister() {
    $("#loginDiv").hide();
    $("#registerDiv").show();
    document.getElementById("primarySubmit").onclick=register;

    document.getElementById("switch").onclick=showLogin;
    document.getElementById("switch").innerHTML="I already have an account"
}

function showLogin() {
    $("#loginDiv").show();
    $("#registerDiv").hide();
    document.getElementById("primarySubmit").onclick=login;

    document.getElementById("switch").onclick=showRegister;
    document.getElementById("switch").innerHTML="Create an account"
}

function login(){
    // Create an FormData object
    var data = new FormData();
    $("#loginError").html("");
    if(!$("#loginEmail").val()||!$("#loginPassword").val()){
        $("#loginError").html("Please fill both fields");
        return;
    }

    // If you want to add an extra field for the FormData
    data.append("email", $("#loginEmail").val());
    data.append("password", $("#loginPassword").val());

    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "api/users/login",
        data: data,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        success: function (data) {
            // console.log("Login --------------------------------------------");
            // console.log(data.id);
            // console.log("Login --------------------------------------------");
            if(data.id){
                $.cookie("email", data.email, { expires : 10 });
                $.cookie("token", data.token, { expires : 10 });
                username = data.username
                // document.getElementById("myAccountButton").innerHTML='Hi, '+$.cookie("email");
                document.getElementById("myAccountButton").innerHTML='Hi, '+username;
                $('#loginModal').modal('hide');
                $("#loginEmail").val("");
                $("#loginPassword").val("");

                $('#myAccount').show();
                $('#login').hide();
                $('#mainMenu').show();
                $('#schedule').show();


                initializeTree();
                $('#elfinder').elfinder({
                    url : 'elfinder/connector'
                });
                if(data.reset)
                    $("#resetModal").modal("show");



            }
            else{
                alertify.notify("Server Error", 'error', 3);
            }
        },
        error: function (e) {
            if(e.status===403)
                alertify.notify("Unauthorized, Try again", 'error', 3);
            else
                alert("Error!"+e.responseText);


        }
    });
}

function  forgot() {
    $("#loginError").html("");
    var data = new FormData();

    if(!$("#loginEmail").val()){
        $("#loginError").html("Please enter email");
        return;
    }

    // If you want to add an extra field for the FormData
    data.append("email", $("#loginEmail").val());

    alertify.notify("Please Wait", 'success', 2);

    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "api/users/forgot",
        data: data,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        success: function () {
            alertify.notify("Reset link sent on Email", 'success', 3);
        },
        error: function (e) {
            if(e.status===403)
                alertify.notify("User does not exist", 'error', 3);
            else
                alertify.notify(e.responseText, 'error', 3);
        }
    });
}

function register(){
    // Create an FormData object
    var data = new FormData();

    if(!$("#registerName").val()||!$("#registerEmail").val()){
        $("#registerError").html("Please fill all fields");
        return;
    }

    // If you want to add an extra field for the FormData
    data.append("email", $("#registerEmail").val());
    data.append("username", $("#registerName").val());
    data.append("password", $("#registerPassword").val());

    alertify.notify("Please Wait", 'success', 2);

    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "api/users/register",
        data: data,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        success: function () {
            alertify.notify("Check your Email for Password", 'success', 3);
            showLogin();
            $("#loginEmail").val($("#registerEmail").val());
            $("#registerEmail").val("");
            $("#registerName").val("");
        },
        error: function (e) {
            if(e.status===403)
                alertify.notify("Account already exists", 'error', 3);
            else
                alertify.notify(e.responseText, 'error', 3);
        }
    });
}

function  reset() {
    $("#resetError").html("");
    var data = new FormData();

    data.append("currentPassword", $("#resetCurrent").val());
    data.append("newPassword", $("#resetNew").val());

    if(!$("#resetCurrent").val()||!$("#resetNew").val()){
        $("#resetError").html("Please fill both fields");
        return;
    }

    if($("#resetNew").val().length<4){
        $("#resetError").html("Please use a longer password");
        return;
    }

    if($("#resetCurrent").val()===$("#resetNew").val()){
        $("#resetError").html("Current and New Password cannot be same!");
        return;
    }

    // If you want to add an extra field for the FormData

    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "api/users/reset",
        data: data,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        beforeSend: function(request) {
            request.setRequestHeader("email",  $.cookie("email"));
            request.setRequestHeader("token",  $.cookie("token"));
        },
        success: function () {
            $("#resetModal").modal('hide');
            $("#resetCurrent").val("");
            $("#resetNew").val("");
            alertify.notify("Password has been reset", 'success', 3);
        },
        error: function (e) {
            if(e.status===403){
                $("#resetError").html("Current Password is incorrect!");
            }
            if(e.status===400){
                alert("Error!"+e.responseText);
            }
            else{
                alertify.notify("Sorry there was an error", 'error', 3);
            }
        }
    });
}

function deleteModule(module){

        // Create an FormData object
        var formData = new FormData();

        formData.append("jarName",module);

        alertify.notify("Please Wait", 'success', 2);

        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "api/workflow/deleteJar",
            data: formData,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            beforeSend: function(request) {
                request.setRequestHeader("email",  $.cookie("email"));
                request.setRequestHeader("token",  $.cookie("token"));
            },
            success: function (data) {
                initializeTree();
                alertify.notify(module+' deleted successfully!', 'success', 5);
            },
            error: function (e) {
                alertify.notify('Error Deleting module', 'error', 3);
                if(e.status===403){
                    alertify.notify(e.responseText, 'error', 10);
                }
                if(e.status===400){
                    alert("Error!"+e.responseText);
                }
            }
        });

}


