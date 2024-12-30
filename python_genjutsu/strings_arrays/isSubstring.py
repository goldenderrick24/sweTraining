class Rotation(object):
    
    def is_sub_str(self, s1, s2):
        return s1 in s2
    
    def rotation(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if len(s1) != len(s2):
            return False
        return self.is_sub_str(s1, s2 + s2)
    

from nose.tools import assert_equal


class TestRotation(object):

    def test_rotation(self):

        rotation = Rotation()

        assert_equal(rotation.is_rotation('o', 'oo'), False)

        assert_equal(rotation.is_rotation(None, 'foo'), False)

        assert_equal(rotation.is_rotation('', 'foo'), False)

        assert_equal(rotation.is_rotation('', ''), True)

        assert_equal(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)

        print('Success: test_rotation')



def main():

    test = TestRotation()

    test.test_rotation()


if __name__ == '__main__':
    main()