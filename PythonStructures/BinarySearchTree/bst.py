from binaryNode import BinaryNode

class BinarySearchTree() :

    def __init__(self) :
        self.length = 0
        self.root = None

    def getRoot(self) : # to comment/remove
        return self.root.getValue()

    def addNode(self, newValue) :
        self.length += 1
        newNode = self.__addNode(newValue, self.root)
        if self.root == None :
            self.root = newNode
        
    def __addNode(self, newValue, node) :
        if node == None :
            node = BinaryNode(newValue)

        elif node.hasEqualValue(newValue) :
            node.setValue(newValue)

        elif node.hasGreaterValue(newValue) :
            node.setLeft(self.__addNode(newValue, node.getLeft()))

        else : # node.hasLesserValue(newValue)
            node.setRight(self.__addNode(newValue, node.getRight()))

        return node

    def removeNode(self, value) :
        self.length -= 1
        self.root = self.__removeNode(value, self.root)

    def __removeNode(self, value, node) :
        if node == None :
            return None    
        
        if node.hasEqualValue(value) :
            # node is the Node to be removed
            if node.getLeft() == None and node.getRight() == None : # node is a leaf (has no childs) 
                return None
            
            if node.getLeft() == None : # has only right child   
                return node.getRight()
            
            if node.getRight() == None : # has only right child   
                return node.getLeft()
            
            minValue = self.__smallestValue(node.getRight())
            node.setValue(minValue)
            node.setRight(self.__remove(minValue, node.getRight()))

        elif node.hasGreaterValue(newValue) :
            node.setLeft(self.__remove(value, node.getLeft()))

        else : # node.hasLesserValue(newValue)
            node.setRight(self.__remove(value, node.getRight()))
        
        return node

    def smallestValue(self) :
        if self.root == None :
            return None

        return self.__smallestValue(self.root)

    def __smallestElement(self, node) :
        if node.getLeft() == None :
            return node.getValue()

        return self.__smallestElement(node.getLeft())

    def inOrder(self) :
        result = []
        if self.root != None :
            self.__inOrder(self.root, result)

        return result

    def __inOrder(self, node, result) :
        if node != None :
            self.__inOrder(node.getLeft(), result)
            result.append(node.getValue())
            self.__inOrder(node.getRight(), result)

    def preOrder(self) :
        result = []
        if self.root != None :
            self.__preOrder(self.root, result)

        return result

    def __preOrder(self, node, result) :
        if node != None :
            result.append(node.getValue())
            self.__preOrder(node.getLeft(), result)
            self.__preOrder(node.getRight(), result)

    def posOrder(self) :
        result = []
        if self.root != None :
            self.__posOrder(self.root, result)

        return result

    def __posOrder(self, node, result) :
        if node != None :
            self.__posOrder(node.getLeft(), result)
            self.__posOrder(node.getRight(), result)
            result.append(node.getValue())

    def nodesByLevel(self) :
        if self.root == None :
            return None 
        
        result = {}
        self.__nodesByLevel(self.root, result, 0)
        return result

    def __nodesByLevel(self, node, result, level) :
        if node != None :
            if level in result :
                result[level].append(node.getValue())
            else :
                result[level] = [node.getValue()]

        level += 1

        if node.getLeft() != None :
            self.__nodesByLevel(node.getLeft(), result, level)

        if node.getRight() != None  :
            self.__nodesByLevel(node.getRight(), result, level)

    def nodesByLevel2(self) :
        if self.root == None :
            return None 
        
        result = {}
        self.__nodesByLevel2(self.root, result, 0)
        result.popitem()
        return result

    def __nodesByLevel2(self, node, result, level) :
        if node != None :
            if level in result :
                result[level].append(node.getValue())
            else :
                result[level] = [node.getValue()]
            
            level += 1

            # if node.getLeft() != None :
            self.__nodesByLevel2(node.getLeft(), result, level)

            # if node.getRight() """!= None  :
            self.__nodesByLevel2(node.getRight(), result, level)

        else :
            if level in result :
                result[level].append(None)
                # result[level + 1].append(-1)
            else :
                result[level] = [None]

    def nodesByLevel3(self) :
        if self.root == None :
            return None 
        
        result = {}
        result[0] = [[self.root.getValue()]]
        self.__nodesByLevel3(self.root, result, 1)
        result.popitem()
        return result

    def __nodesByLevel3(self, node, result, level) :
        if not level in result :
            result[level] = []
            
        pair = []
    
        left_node = node.getLeft()
        right_node = node.getRight()
    
        has_left : bool = left_node != None

        if has_left :
            self.__nodesByLevel3(left_node, result, level + 1)
            pair.append(left_node.getValue())

        if right_node != None :
            self.__nodesByLevel3(right_node, result, level + 1)
            
            if not has_left :
                pair.append(right_node.getValue())
            pair.append(right_node.getValue())
            
        result[level].append(pair)

    def __repr__(self) :
        result = ""
        return self.__reprHelper(self.root, 0, result)
        # return result

    def __reprHelper(self, node, level : int, result : str) :
        if node != None :
            result = self.__reprHelper(node.getRight(), level + 1, result)
            if level != 0 :
                for i in range(0, level - 1) : 
                    result += "|   "
                result += "+--%s\n" % (str(node.getValue()))
            else :
                result += "%s\n" % (str(node.getValue()))
            result = self.__reprHelper(node.getLeft(), level + 1, result)
        return result
