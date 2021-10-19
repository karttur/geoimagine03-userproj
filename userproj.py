'''
Created on 3 Mar 2021

@author: thomasgumbricht
'''

class ProcessUserProj():
    '''class for managing users, projects and tracts
    '''  
     
    def __init__(self, pp, session):
        '''
        '''
        
        self.session = session
                
        self.pp = pp  
        
        self.verbose = self.pp.process.verbose 
        
        self.session._SetVerbosity(self.verbose)

        if self.verbose > 0:

            print ('        ProcessUserProj',self.pp.process.processid) 
            
        if self.pp.process.processid.lower() == 'managedefregproj':
            
            self._ManageDefRegProj()
            
    def _ManageDefRegProj(self):
        '''
        '''
                
        tractidparts = self.pp.process.parameters.tractid.split('-')
        
        if len(tractidparts) >= 2 and len(tractidparts[0]) >= 4 and len(tractidparts[1]) >= 4:
            
            pass
            
        else:
            exitstr = 'The user tracid nust contain at least one hyphen and at least 4 letters on each side of the hyphen'
            
            exit(exitstr)
            
        projidparts = self.pp.process.parameters.projid.split('-')
        
        if len(projidparts) >= 2 and len(projidparts[0]) >= 4 and len(projidparts[1]) >= 4:
            
            pass
            
        else:
            
            exitstr = 'The projid must contain at least one hyphen and at least 4 letters on each side of the hyphen'
            
            exit(exitstr)   
                  
        queryD = dict( list( self.pp.process.parameters.__dict__.items() ) )
                    
        queryD['userid'] = self.pp.userproject.userid #self.process.proc.userProj.userid
        
        queryD['siteid'] = queryD['tractid']
        
        queryD['sitename'] = queryD['tractname']
        
        queryD['sitetitle'] = queryD['tracttitle']
        
        queryD['sitelabel'] = queryD['tractlabel']
        
        queryD['regiontype'] = 'D'
            
        self.session._ManageDefRegProjTractSite(queryD)
            
            