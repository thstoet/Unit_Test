
class Faku:

    def fact1(self, n):
        self.m = n
        if self.m == 1:
            return 1
        else:
            return self.m*Faku.fact1(self, n-1)

if __name__ == "__main__":

    Test = Faku()
    print(Test.fact1(4))