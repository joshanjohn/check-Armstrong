str1=input("enter the STRING:")
st=str1
st=st.casefold()
revst=reversed(st)
if list(st) == list(revst):
    print(str1,"is palindrome")
else:
    print(str1,"not palindrome")
