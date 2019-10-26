from pyautocad import Autocad, APoint


acad = Autocad()       #Connects Python to 
acad.prompt("Hello, Autocad from Python\n")
#acad.doc returns ActiveDocument: Returns a Document object that represents the the document with the focus. If there are no documents open, an error occurs. 
print (acad.doc.Name)


#Our example command is to draw a line from (0,0) to (5,5)
# command_str = 'ucs z 90 ' #Notice that the last SPACE is equivalent to hiting ENTER
#You should separate the command's arguments also with SPACE

#Send the command to the drawing
# acad.doc.SendCommand(command_str)

# p1 = APoint(0, 0)
# p2 = APoint(50, 25)
# for i in range(5):
#     text = acad.model.AddText('Hi %s!' % i, p1, 2.5)
#     acad.model.AddLine(p1, p2)
#     acad.model.AddCircle(p1, 10)
#     p1.y += 10

# dp = APoint(10, 0)
# for text in acad.iter_objects('Text'):
#     print('text: %s at: %s' % (text.TextString, text.InsertionPoint))
#     text.InsertionPoint = APoint(text.InsertionPoint) + dp

# for obj in acad.iter_objects(['Circle', 'Line']):
#     print(obj.ObjectName)