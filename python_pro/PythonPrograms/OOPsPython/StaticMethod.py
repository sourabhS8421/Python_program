class STMethod:
    pass

    #Efficient than using self
    @staticmethod
    def display_beheviour(string):
        print("You're so " + string)

behaviour = STMethod()

behaviour.display_beheviour("strong")