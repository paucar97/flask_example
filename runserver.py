from app import api
import sys
if __name__ == '__main__':
    if (len(sys.argv)>=2):
        if (sys.argv[1] == "db"):
            print("ENTRO AL MANAGER")
            api.manager.run() # para usar el migrate 
        else:
            api.app.run(host="0.0.0.0", port=5000, debug=True) #levantar el back
    else:
        api.app.run(host="0.0.0.0", port=5000, debug=True) #levantar el back
