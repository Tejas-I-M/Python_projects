class LogAnalyzer:
    def __init__(self,file_name):
        self.file_name = file_name
    def analyze(self):
        try:
            with open(self.file_name,"r") as f:
                lines = f.readlines() 
        except FileNotFoundError:
            print("file not found")
            return
        total=len(lines)
        info=0
        error=0
        warning=0
        error_messages=[]
        for line in lines:
            if line.startswith("INFO"):
                info+=1
            elif line.startswith("ERROR"):
                error+=1
                error_messages.append(line.strip())
            elif line.startswith("WARNING"):
                warning+=1
        print("\nLog analyzer")
        print("total: ",total)
        print("info: ",info)
        print("error: ",error)
        print("warning: ",warning)
        print("\n Error details: ")
        for msg in error_messages:
            print("-",msg)
lg=LogAnalyzer('log.txt')
lg.analyze()