# -*- coding: utf-8 -*-
def MainHeader(node, gravity=[0.0, -9.8, 0.0], dt=0.01, plugins=[], repositoryPaths=[]):
        '''
        Args:
            gravity (vec3f): define the gravity vector.

            dt  (float): define the timestep.

            plugins (list str): list of plugins to load

            repositoryPaths (list str): list of path to the specific data repository

        Structure:
            .. sourcecode:: qml

                rootNode : {
                    gravity : gravity,
                    dt : dt,
                    VisualStyle,
                    RepositoryPath,
                    RequiredPlugin,
                    OglSceneFrame,
                    FreeMotionAnimationLoop,
                    GenericConstraintSolver,
                    DefaultContactManager
                    DiscreteIntersection
                }

        '''
	node.createObject('VisualStyle', displayFlags='showVisualModels showBehaviorModels showCollisionModels showForceFields showInteractionForceFields')

        i=0
        for repository in repositoryPaths:
            node.createObject('AddResourceRepository', name="AddResourceRepository"+str(i), path=repository)
            i+=1

        node.findData('gravity').value=gravity;
    	node.findData('dt').value=0.01

        if "SofaMiscCollision" not in plugins:
            plugins.append("SofaMiscCollision")

        if "SofaPython" not in plugins:
            plugins.append("SofaPython")

 	for name in plugins:
	 	node.createObject('RequiredPlugin', name=name)
	 	
    	node.createObject('OglSceneFrame', style="Arrows", alignment="TopRight")

        node.createObject('FreeMotionAnimationLoop')
        node.createObject('GenericConstraintSolver', tolerance="1e-6", maxIterations="1000")


### This function is just an example on how to use the DefaultHeader function. 
def createScene(rootNode):
        import os
	MainHeader(rootNode, plugins=["SofaMiscCollision","SofaPython","SoftRobots"], repositoryPaths=[os.getcwd()])
	
    
