import json

class Helper:

    @staticmethod
    def load_file(ruta_json): 

        try:
            with open(ruta_json, 'r') as archivo: 
                    return json.load(archivo)
        except FileNotFoundError:
            return None, print("Archivo no encontrado.")
        
    @staticmethod    
    def save_file(ruta_json, item):
            
            with open(ruta_json, 'w') as archivo:
                json.dump(item, archivo)


    @staticmethod
    def save_in_list(ruta_json, item):
            
            List = Helper.load_file(ruta_json)
            List.append(item)
            Helper.save_file(ruta_json,List)
            
    @staticmethod
    def delete_item(ruta_json, item):

        List = Helper.load_file(ruta_json)
        
        if List is not None:
            if item in List:
                
                List.remove(item)
                Helper.save_file(ruta_json, List)
            else:
                 print("Elemento no encontrado..")
        else:
             return None
"""
    @staticmethod
    def modify_item(ruta_json, item_id):
         
         List = Helper.load_file(ruta_json)
         if List is not None:
            for data in List:
                if data['id']==item_id:
                     

                
                Helper.save_file(ruta_json, List)
            else:
                 print("Elemento no encontrado..")
         else:
            return None
            """