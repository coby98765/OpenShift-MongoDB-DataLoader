class Utils:

    @staticmethod
    def correct_the_id(result):
        for organ in result["result"]:
            organ['_id'] = str(organ['_id'])
        return result

