let data = [];
let createNotification = function (text) {

};
Vue.component('move', {
    props: ['tomoves'],
    template: '<ul><li v-for="item in tomoves"><a target="_blank" :href="[[ item ]]" v-html="item"></a></li></ul>'
})
let app = new Vue({
    delimiters: ["[[", "]]"],
    el: '#daily-chess',
    data: {
        tomoves: []
    },
    watch: {
        tomoves: function (newMove, oldMove) {
            console.log(oldMove)
            if (newMove.length > oldMove.length) {
                let nonNotifiedMoves = _.difference(newMove, oldMove)
                console.log(nonNotifiedMoves)
                let firstMove = _.first(newMove)
                new Notification("A new move is available", {
                    body: firstMove,
                    icon: this.icon
                })
            }
        }
    },
    mounted: function () {
        this.icon = this.$el.attributes.icon.value;
        let self = this;
        setInterval(function () {
            $.ajax({
                url: "/admin/client/game/tomove",
                cache: false,
                dataType: 'json'
            }).done(function (res) {
                self.tomoves = res
            });
        }, 5000);
    }
})
