class BinaryNode() :

    def __init__(self, value) :
        self.value = value
        self.right : BinaryNode = None
        self.left : BinaryNode = None

    def setRight(self, rightValue) :
        if isinstance(rightValue, BinaryNode) :
            self.right = rightValue
        else :
            self.right = BinaryNode(rightValue)

    def setLeft(self, leftValue) :
        if isinstance(leftValue, BinaryNode) :
            self.left = leftValue
        else :
            self.left = BinaryNode(leftValue)

    def setValue(self, newValue) :
        self.value = newValue

    def getRight(self) :
        return self.right

    def getLeft(self) :
        return self.left

    def getValue(self) :
        return self.value

    def hasEqualValue(self, otherValue) :
        return self.value.__eq__(otherValue)

    def hasGreaterValue(self, otherValue) :
        return self.value.__gt__(otherValue) 

    def hasLesserValue(self, otherValue) :
        return self.value.__lt__(otherValue) 