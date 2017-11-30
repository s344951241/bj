public class RobotConfig
{
    static int[] _Keys;
    static SortedList<int,RobotConfig> _Data;
    public int Id;
    public string Type;
    public int BodyId;
    public Table SlotEquips;
    public float Value;

    public static void SetData(string text)
    {
        RobotConfig data = new RobotConfig();
        string[] tokens = Table.GetTokens(text);
        int.TryParse(tokens[0],out data.Id);
        if(tokens[1]!=null)
            data.Type = tokens[1].Substring(1,tokens[1].Length-2);
        int.TryParse(tokens[2],out data.BodyId);
        if(tokens[3]!=null)
            data.SlotEquips = new Table(tokens[3]);
        float.TryParse(tokens[4],out data.Value);
        _Data[data.Id] = data;

    }

    public static RobotConfig GetConfig(int id)
    {
        if(_Data==null)
            LoadConfig();
        RobotConfig dat = null;
        _Data.TryGetValue(id,out data);
        return data;
    }
    public static int [] GetKeys()
    {

        if(_Data==null)
            LoadConfig();
        if(_Keys==null)
        {
            IList<int> keys = _Data.keys;
            _Keys = new int[_Data.Count];
            for(int i=0;i<_Keys.Length;i++)
            {
                _Keys[i] = keys[i];
            }
            return _Keys;
        }
    }

    static void LoadConfig()
    {
        _Data = new SortedList<int,RobotConfig>();
        string text = ConfigManager.GetData("RobotConfig");
        string [] rows = text.Split('\n');
        int count = rows.Length-1;
        for(int i=0;i<count;i++)
            SetData(rows[i]);
    }
}