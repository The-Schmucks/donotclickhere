package com.example.myapplication;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Bundle;
import android.provider.Settings;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class MainActivity extends AppCompatActivity {

    private EditText editText;
    private MessageAdapter messageAdapter;
    private ListView messagesView;
    private static Context context;

    public static Context getcontext() {
        return MainActivity.context;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        MainActivity.context = getApplicationContext();

        editText = (EditText) findViewById(R.id.editText);

        messageAdapter = new MessageAdapter(this);
        messagesView = (ListView) findViewById(R.id.messages_view);
        messagesView.setAdapter(messageAdapter);

        MemberData data = new MemberData("Clovis", getRandomColor());
    }

    public void get_answer(String command) {

        command = command.replace(" ", "%20");
        String url = "http://192.168.1.196:5000/api/v1?command=" + command;
        RequestQueue req_queue = Volley.newRequestQueue(MainActivity.getcontext());
        JsonObjectRequest obj_request = new JsonObjectRequest(
                Request.Method.GET,
                url,
                null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            Map<String, Object> results = new HashMap<String, Object>();
                            results.put("answer", response.getString("answer"));
                            results.put("audio", response.getString("audio"));
                            results.put("is_command", response.getBoolean("is_command"));

                            onMessage(results);
                            //Log.e("Success Response", results.toString());
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.e("Error Response", error.toString());
                    }
                }
        );
        req_queue.add(obj_request);
    }

    public void sendMessage(View view) {
        String sentMessage = editText.getText().toString();
        if (sentMessage.length() > 0) {
            final MemberData data = new MemberData("Clovis/User", "navy");
            final Message message = new Message(sentMessage, "none", data, true);

            messageAdapter.add(message);
            get_answer(sentMessage);
            editText.getText().clear();
        }
    }

    public void onMessage(Map<String, Object> results) {

        //Log.e("results in Messages ", results.toString());

        final String audio = String.valueOf(results.get("audio"));
        final String answer = String.valueOf(results.get("answer"));
        final Boolean is_command = ((Boolean)results.get("is_command"));
        // member.clientData is a MemberData object, let's parse it as such
        final MemberData data = new MemberData("kadogo", "red");
        // since the message body is a simple string in our case we can use json.asText() to parse it as such
        // if it was instead an object we could use a similar pattern to data parsing
        String receivedMessage = final_responce(answer, is_command);
        final Message message = new Message(receivedMessage, audio, data, false);
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                messageAdapter.add(message);
                // scroll the ListView to the last added element
                messagesView.setSelection(messagesView.getCount() - 1);
                if(is_command == true){
                    redirect(answer);
                }
            }
        });
    }

    private void redirect(String answer){
        Uri webpage = Uri.parse(answer);
        Intent webIntent = new Intent(Intent.ACTION_VIEW, webpage);
        startActivity(webIntent);
    }
    private String final_responce(String answer, Boolean is_command){
        if(is_command == true){
            return "Done";
        }
        return answer;
    }
    private String getRandomColor() {
        Random r = new Random();
        StringBuffer sb = new StringBuffer("#");
        while(sb.length() < 7){
            sb.append(Integer.toHexString(r.nextInt()));
        }
        return sb.toString().substring(0, 7);
    }
}
