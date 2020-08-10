import pytest

class InsufficientException(Exception):
  pass

class MobileInventory():
    balance_inventory = {}
    def __init__(self,inventory):
        if not(isinstance(inventory,dict)):
            raise TypeError("Input inventory must be a dictionary")
        key_type = set(map(type, inventory.keys()))
        if not ( key_type == {str} or key_type == set()):
            raise ValueError("Mobile model name must be a string")
        val_type = set(map(type, inventory.values()))
        if not (val_type == {int} or val_type == set()):
            raise ValueError("No. of mobiles must be a positive integer")
        neg_values = [i for i in inventory.values() if i < 0]
        if len(neg_values) != 0:
            raise ValueError("No. of mobiles must be a positive integer")
        self.balance_inventory = inventory
        
        
    def add_stock(self,new_stock):
        if not(isinstance(new_stock,dict)):
            raise TypeError("Input stock must be a dictionary")
        key_type = set(map(type, new_stock.keys()))
        if not (key_type == {str} or key_type == set()):
            raise ValueError("Mobile model name must be a string")
        val_type = set(map(type, new_stock.values()))
        if not (val_type == {int} or val_type == set()):
            raise ValueError("No. of mobiles must be a positive integer")
        neg_values = [i for i in new_stock.values() if i < 0]
        if len(neg_values) != 0:
            raise ValueError("No. of mobiles must be a positive integer")
        for r_k,r_v in new_stock.items():
            modelFound = False
            for i_k,i_v in self.balance_inventory.items():
                if r_k == i_k:
                    modelFound=True
                    self.balance_inventory[r_k] = int(i_v+r_v)
                    break
            if modelFound == False:
               self.balance_inventory[r_k] = r_v
    
    def sell_stock(self,requested_stock):
        if not(isinstance(requested_stock,dict)):
            raise TypeError("Requested stock must be a dictionary")
        key_type = set(map(type, requested_stock.keys()))
        if not (key_type == {str} or key_type == set()):
            raise ValueError("Mobile model name must be a string")
        val_type = set(map(type, requested_stock.values()))
        if not (val_type == {int} or val_type == set()):
            raise ValueError("No. of mobiles must be a positive integer")
        neg_values = [i for i in requested_stock.values() if i < 0]
        if len(neg_values) != 0:
            raise ValueError("No. of mobiles must be a positive integer")
        
        for r_k,r_v in requested_stock.items():
            modelFound=False
            insufficientInventory=False
            for i_k,i_v in self.balance_inventory.items():
                if r_k == i_k:
                    modelFound=True
                    if r_v > i_v:
                        insufficientInventory=True
                        break
                    self.balance_inventory[r_k] = int(i_v-r_v)
                    break
            if modelFound == False:
                raise InsufficientException("No Stock. New Model Request")
            if insufficientInventory == True:
                raise InsufficientException("Insufficient Stock")

#import pytest
#from proj.inventory import MobileInventory, InsufficientException

class TestingInventoryCreation():
    def test_creating_empty_inventory(self):
        m = MobileInventory({})
        assert m.balance_inventory == {}
        
    def test_creating_specified_inventory(self):
        m = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
    
    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError) as e:
            m = MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
        assert "Input inventory must be a dictionary" in str(e.value)
    
    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(ValueError) as e:
            m = MobileInventory({1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
        assert "Mobile model name must be a string" in str(e.value)

    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as e:
            m = MobileInventory({'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'})
        assert "No. of mobiles must be a positive integer" in str(e.value)

    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError) as e:
            m = MobileInventory({'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25})
        assert "No. of mobiles must be a positive integer" in str(e.value)


class TestInventoryAddStock():
    inventory = object
    @classmethod
    def setup_class(cls):
        TestInventoryAddStock.inventory = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        
    def test_add_new_stock_as_dict(self):
        TestInventoryAddStock.inventory.add_stock({'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10})
        assert TestInventoryAddStock.inventory.balance_inventory == {'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25, 'Nokia Model A':10}
    
    def test_add_new_stock_as_list(self):
        with pytest.raises(TypeError) as e:
            TestInventoryAddStock.inventory.add_stock(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
        assert "Input stock must be a dictionary" in str(e.value)

    def test_add_new_stock_with_numeric_keys(self):
        with pytest.raises(ValueError) as e:
            TestInventoryAddStock.inventory.add_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
        assert "Mobile model name must be a string" in str(e.value)

    def test_add_new_stock_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as e:
            TestInventoryAddStock.inventory.add_stock({'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'})
        assert "No. of mobiles must be a positive integer" in str(e.value)

    def test_add_new_stock_with_float_values(self):
        with pytest.raises(ValueError) as e:
            TestInventoryAddStock.inventory.add_stock({'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25})
        assert "No. of mobiles must be a positive integer" in str(e.value)


class TestInventorySellStock():
    inventory = object
    @classmethod
    def setup_class(cls):
        TestInventorySellStock.inventory = MobileInventory({'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        
    def test_sell_stock_as_dict(self):
        TestInventorySellStock.inventory.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1})
        assert TestInventorySellStock.inventory.balance_inventory == {'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0}
    
    def test_sell_stock_as_list(self):
        with pytest.raises(TypeError) as e:
            TestInventorySellStock.inventory.sell_stock(['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'])
        assert "Requested stock must be a dictionary" in str(e.value)

    def test_sell_stock_with_numeric_keys(self):
        with pytest.raises(ValueError) as e:
            TestInventorySellStock.inventory.sell_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
        assert "Mobile model name must be a string" in str(e.value)

    def test_sell_stock_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as e:
            TestInventorySellStock.inventory.sell_stock({'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'})
        assert "No. of mobiles must be a positive integer" in str(e.value)

    def test_sell_stock_with_float_values(self):
        with pytest.raises(ValueError) as e:
            TestInventorySellStock.inventory.sell_stock({'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4})
        assert "No. of mobiles must be a positive integer" in str(e.value)

    def test_sell_stock_of_nonexisting_model(self):
        with pytest.raises(InsufficientException) as e:
            TestInventorySellStock.inventory.sell_stock({'iPhone Model B':2, 'Xiaomi Model B':5})
        assert "No Stock. New Model Request" in str(e.value)

    def test_sell_stock_of_insufficient_stock(self):
        with pytest.raises(InsufficientException) as e:
            TestInventorySellStock.inventory.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15})
        assert "Insufficient Stock" in str(e.value)



