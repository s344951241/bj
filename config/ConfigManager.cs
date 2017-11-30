public class ConfigManager
{
    public static Dictionary<string,string> _Data = new Dictionary<string,string>();

    public static void SetData(TextAsset textAsset)
    {
        if(textAsset==null)
            return;
        _Data[TextAsset.name] = textAsset.text;
    }

    public static string GetData(string name)
    {
        string text = null;
#if NO_AB
        if(text==null)
        {
            //加载TODO
        }
#else
        _Data.TryGetValue(name,out text);
#endif
        return text;
    }
}