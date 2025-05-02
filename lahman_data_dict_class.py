import ootp_lahman_utils as utils

class LahmanDict(dict):
    """
    """

    def __init__(self, dict_type, lahman_path=None):
        """

        :type self: object
        :rtype : None
        :param dict_type: type of lahman database ('batting', 'pitching', 'fielding', 'master')
        :param lahman_path: path to the lahman file to import
        
        """
        lahman_dict = dict() # initialize dictionary of lahman data
        self.dict_type = dict_type

        # if no lahman path is specified, initialize an empty lahman dictionary
        if lahman_path:
            dict.__init__(lahman_dict)
            return

        else:
            # if a lahman file path is specified, open the file
            try:
                f = open(lahman_path)

            # if file does not exist, initialize an empty lahman dictionary

            except OSError:
                print "File '" + lahman_path + "' does not exist.  Initializing empty Lahman dictionary."
                dict.__init__(lahman_dict)
                return

        # lahman data file is open

        lahman_dicts = Utils.import_lahman_data_file(lahman_path, dict_type, verbose=True)

        self.data_dict = lahman_dicts['data']
        self.header_dict = lahman_dicts['header']
        self.lookup_dict = lahman_dicts['lookup']

        return
