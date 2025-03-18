from android_setup import AndroidSetup
import time

class SwipeTests(AndroidSetup):
    def test_swipe_right_to_left(self):
        self.swipe(self.width * 0.9, self.height * 0.5, self.width * 0.1, self.height * 0.5)
        time.sleep(2)

if __name__ == "__main__":
    test = SwipeTests()
    test.test_swipe_right_to_left()
    test.tearDown()