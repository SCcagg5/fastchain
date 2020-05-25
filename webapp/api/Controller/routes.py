from .routesfunc import *

def setuproute(app, call):
    @app.route('/test/',                ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])                                        )
    @app.route('/login/',    	        ['OPTIONS', 'POST'],        lambda x = None: call([getauth])                                 )
    @app.route('/user/signup/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([myauth, signup, signin, gettoken])        )
    @app.route('/user/signin/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([myauth, signin, gettoken])                )
    @app.route('/user/renew/',    	    ['OPTIONS', 'GET'],         lambda x = None: call([myauth, authuser, gettoken])              )
    @app.route('/token/send/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([myauth, authuser, sendtok])               )
    @app.route('/wallet/',    	        ['OPTIONS', 'GET'],         lambda x = None: call([myauth, authuser, wallet])                )
    @app.route('/wallet/create/',    	['OPTIONS', 'GET'],         lambda x = None: call([myauth, authuser, wallet])                )
    @app.route('/wallet/cred/',    	    ['OPTIONS', 'GET'],         lambda x = None: call([myauth, authuser, walletcred])            )
    @app.route('/action/',    	        ['OPTIONS', 'GET'],         lambda x = None: call([myauth, authuser, walletcred])            )
    @app.route('/action/gen/',    	    ['OPTIONS', 'POST'],         lambda x = None: call([createdoc])             )
    def base():
        return
