#input s="aabbbccdddd" output s=a2b3c3d4
class compression:
    def compress_str(self,s):
        result = ""
        count = 1
        for i in range(1,len(s)+1):
            if i <len(s) and s[i]==s[i-1]:
                count +=1
            else:
                result += s[i-1] + str(count)
                count =1
        return result

obj = compression()
print(obj.compress_str("aabbbccdddd"))
