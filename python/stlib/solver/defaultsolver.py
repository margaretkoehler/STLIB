# -*- coding: utf-8 -*-

def DefaultSolver(node):
    '''
    Adds EulerImplicit, CGLinearSolver

    Components added:
        EulerImplicit
        CGLinearSolver
    '''
    node.createObject('EulerImplicit', name='timeintegration', firstOrder='1')
    node.createObject('CGLinearSolver', name='numericsolver')


### This function is just an example on how to use the DefaultHeader function. 
def createScene(rootNode):
	DefaultSolver(rootNode) 	
    
