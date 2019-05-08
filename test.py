import unittest
import controller as controller
import const as const

class TestK_means(unittest.TestCase):
    def SizeSamplesTest(self):
         self.assertEqual(len(controller.define_samples()),const.number_samples)
         samples = controller.define_samples()
          
    def SizeCentroidTest(self):
         samples = controller.define_samples()
         self.assertEqual(len(controller.define_centroids(samples)),const.k)
         
         


if __name__ == '__main__':
    unittest.main()