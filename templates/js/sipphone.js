{% load static %}
//import SIP from '{% static "js/jssip-0.2.0.min.js" %}'

JsSIP.debug.enable ('JsSIP: *');
var socket = new JsSIP.WebSocketInterface('ws://srvpbx.ath.ru:8088/ws');
//socket.via_transport = "tcp";
var token = '{{csrf_token}}';

var configuration = {

    sockets  : [ socket ],
    uri      : 'sip:{{ user.aduser.telephoneNumber }}2@srvpbx.ath.ru',
    password : '{{ password }}'
  };


  var eventHandlers = {
    'progress': function(e) {
      console.log('call is in progress');
    },
    'failed': function(e) {
      console.log('call failed with cause: '+ e.data);
    },
    'ended': function(e) {
      console.log('call ended with cause: '+ e);
    },
    'confirmed': function(e) {
      console.log('call confirmed');
    }
  };
  /*uri:                '{{ user.aduser.telephoneNumber }}1@{{ server }}',
  ws_servers:         'ws://{{ server }}:8088/ws',
  ws_uri:       'ws://{{ server }}:8088/ws',
  authorizationUser:    '{{ user.aduser.telephoneNumber }}1',
  password:           '{{ password }}',
  hackIpInContact: true,

  // rtcpMuxPolicy for Asterisk
  rtcpMuxPolicy: 'negotiate',
};*/

var ua = new JsSIP.UA(configuration);


ua.start();

var options = {
  'eventHandlers'    : eventHandlers,
  'mediaConstraints' : { 'audio': true, 'video': false }
};

var session = ua.call('sip:6350@{{ server }}:5060', options);
/*var session = ua.call('sip:66331', options);
var session = ua.call('sip:66331@srvpbx.ath.ru:5060', options);
var session = ua.call('sip:66331@srvpbx.ath.ru', options);
var session = ua.call('sip:66331@{{ server }}', options);
var session = ua.call('sip:66331@device', options);
var session = ua.call('sip:sip/66331@device', options);
var session = ua.call('sip:sip/66331@{{ server }}', options);
var session = ua.call('sip:sip/66331@{{ server }}:5060', options);

/*ua.invite('6633@{{ server }}',{
  media: {
    constraints: {
      audio: true,
      video: false
    }
  }
});
*/
